from flask import Flask, render_template, flash, redirect, session, g, jsonify,url_for
from flask_debugtoolbar import DebugToolbarExtension
from forms import MoneyEventForm, AirTravelEventForm, DistanceEventForm, RegisterForm, LoginForm, EditProfileForm
from models import db, connect_db, User, UserActivity
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
import requests
import json
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
# app.config.from_object('config.DevConfig')
debug = DebugToolbarExtension(app)
CORS(app)
connect_db(app)



##################################################################################################
"""General"""


CURR_USER_KEY = "curr_user"
token = os.environ.get('BEARER')
base_url = os.environ.get('BASE_URL')
HEADERS = { "Authorization": "Bearer " + token }

def format_payload(e_id, param1_label, param1_data, param2_label, param2_data):
    """Format payload sent to Climatiq from Add Activity Form"""
    return {
      "emission_factor": e_id,
        "parameters":
          {
          param1_label: param1_data,
          param2_label: param2_data
          }
    }

def format_payload_flight(from_data, to_data):
    """Format payload for flights sent to Climatiq from Add Activity Form"""
    return {
      "legs": [
          {
          "from": from_data,
          "to": to_data
          }
      ]
    }

@app.before_request
def add_user_to_g():

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


@app.errorhandler(404)
def page_not_found(e):

    return render_template('404.html'), 404


@app.route('/')
def homepage():

    if g.user:
        user = User.query.filter_by(id = g.user.id).first()
        total_co2e = UserActivity.sum_all(g.user.id)
        total_co2e_flights = UserActivity.sum_all_flights(g.user.id)
        total_co2e_driving = UserActivity.sum_all_drives(g.user.id)
        total_co2e_clothing = UserActivity.sum_all_clothing(g.user.id)
        total_co2e_bottles = UserActivity.sum_all_bottles(g.user.id)
        return render_template('index.html',
                                user=user,
                                total_co2e=total_co2e,
                                total_co2e_flights=total_co2e_flights,
                                total_co2e_driving=total_co2e_driving,
                                total_co2e_clothing=total_co2e_clothing,
                                total_co2e_bottles=total_co2e_bottles)

    else:
        return render_template('index-anon.html')


##################################################################################################
""" User Sign-up, Sign-in, Profile Edit, & Logout"""


@app.route('/signup', methods=["GET", "POST"])
def signup():

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

    form = RegisterForm()

    if form.validate_on_submit():
        user = User.register(
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data,
            email=form.email.data,
        )

        db.session.commit()
        session[CURR_USER_KEY] = user.id
        flash(f"Welcome, {user.username}! Add an activity to start tracking.", "success")

        return redirect("/")

    else:
        return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            session[CURR_USER_KEY] = user.id
            flash(f"Welcome back, {user.username}!", "success")

            return redirect("/")

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
        flash(f"Goodbye!", "success")

        return redirect("/")



@app.route('/edit-profile', methods=["GET", "POST"])
def edit_user_profile():

    if not g.user:
        flash("Access unauthorized. Please login.", "error")
        return redirect("/")

    user = g.user
    form = EditProfileForm(obj=user)

    if form.validate_on_submit():
        if User.authenticate(user.username, form.password.data):
            user.username = form.username.data
            user.email = form.email.data
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.image_url = form.image_url.data or "/static/images/user.png"
            user.location = form.location.data
            user.mode_of_transport = form.mode_of_transport.data

            db.session.commit()
            return redirect("/")

        flash("Wrong password. Please try again.", "error")

    return render_template('user-edit.html', form=form)


##################################################################################################
"""Add, Edit, View, & Delete User Activities"""

@app.route('/add-activity', methods=["GET"])
def form():
    """Main Add Activity Render"""
    form_money = MoneyEventForm()
    form_distance = DistanceEventForm()
    form_air_travel = AirTravelEventForm()

    return render_template('activity-add.html',
        form_money=form_money,
        form_distance=form_distance,
        form_air_travel=form_air_travel)


"""Several Miles of Repeating View Functions"""

@app.route('/post-activity-clothing', methods=["POST"])
def add_new_event_clothing():

    form = MoneyEventForm()

    if form.validate_on_submit():
        emission_factor_id = "consumer_goods-type_clothing"
        param1_label = "money"
        param1_data = float(form.spend_qty.data)
        param2_label = "money_unit"
        param2_data = "usd"
        payload = format_payload(emission_factor_id, param1_label, param1_data, param2_label, param2_data)
        r = requests.post(base_url + "/estimate", data=json.dumps(payload), headers=HEADERS)
        co2_e = r.json()["co2e"]

        newevent = UserActivity(
            user_id = session[CURR_USER_KEY],
            activity_id = "Clothing Purchase",
            emission_factor_id = emission_factor_id,
            date = form.date.data,
            IATA_from = None,
            IATA_to = None,
            spend_qty = param1_data,
            spend_unit = param2_data,
            co2e = co2_e
        )

        db.session.add(newevent)
        db.session.commit()

        user = User.query.get_or_404(session[CURR_USER_KEY])
        events = UserActivity.query.filter(UserActivity.user_id == session[CURR_USER_KEY])

        return render_template('activity-view.html', user=user, events=events)


@app.route('/post-activity-bottles', methods=["POST"])
def add_new_event_bottles():

    form = MoneyEventForm()

    if form.validate_on_submit():
        emission_factor_id = "consumer_goods-type_soft_drinks_bottled_water_ice"
        param1_label = "money"
        param1_data = float(form.spend_qty.data)
        param2_label = "money_unit"
        param2_data = "usd"
        payload = format_payload(emission_factor_id, param1_label, param1_data, param2_label, param2_data)
        r = requests.post("https://beta3.api.climatiq.io/estimate", data=json.dumps(payload), headers=HEADERS)
        co2_e = r.json()["co2e"]

        newevent = UserActivity(
            user_id = session[CURR_USER_KEY],
            activity_id = "Plastic Bottle Purchase",
            emission_factor_id = emission_factor_id,
            date = form.date.data,
            IATA_from = None,
            IATA_to = None,
            spend_qty = param1_data,
            spend_unit = param2_data,
            co2e = co2_e
        )

        db.session.add(newevent)
        db.session.commit()

        user = User.query.get_or_404(session[CURR_USER_KEY])
        events = UserActivity.query.filter(UserActivity.user_id == session[CURR_USER_KEY])

        return render_template('activity-view.html', user=user, events=events)


@app.route('/post-activity-driving', methods=["POST"])
def add_new_event_driving():

    form = DistanceEventForm()

    if form.validate_on_submit():
        emission_factor_id = "passenger_vehicle-vehicle_type_motorcycle-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na"
        param1_label = "distance"
        param1_data = float(form.spend_qty.data)
        param2_label = "distance_unit"
        param2_data = "mi"
        payload = format_payload(emission_factor_id, param1_label, param1_data, param2_label, param2_data)
        r = requests.post(base_url + "/estimate", data=json.dumps(payload), headers=HEADERS)
        co2_e = r.json()["co2e"]

        newevent = UserActivity(
            user_id = session[CURR_USER_KEY],
            activity_id = "Driving",
            emission_factor_id = emission_factor_id,
            date = form.date.data,
            IATA_from = None,
            IATA_to = None,
            spend_qty = param1_data,
            spend_unit = param2_data,
            co2e = co2_e
        )

        db.session.add(newevent)
        db.session.commit()

        user = User.query.get_or_404(session[CURR_USER_KEY])
        events = UserActivity.query.filter(UserActivity.user_id == session[CURR_USER_KEY])

        return render_template('activity-view.html', user=user, events=events)


@app.route('/post-activity-air-travel', methods=["POST"])
def add_new_event_airtravel():

    form = AirTravelEventForm()

    if form.validate_on_submit():
        from_data = form.start_airport.data
        to_data = form.land_airport.data
        payload = format_payload_flight(from_data, to_data)
        r = requests.post(base_url + "/travel/flights", data=json.dumps(payload), headers=HEADERS)
        co2_e = r.json()["co2e"]

        newevent = UserActivity(
            user_id = session[CURR_USER_KEY],
            activity_id = "Flying",
            emission_factor_id = "NA",
            date = form.date.data,
            IATA_from = from_data,
            IATA_to = to_data,
            spend_qty = None,
            spend_unit = "flying", #set nullable=true in models
            co2e = co2_e
        )

        db.session.add(newevent)
        db.session.commit()

        user = User.query.get_or_404(session[CURR_USER_KEY])
        events = UserActivity.query.filter(UserActivity.user_id == session[CURR_USER_KEY])

        return render_template('activity-view.html', user=user, events=events)


@app.route('/view-history', methods=["GET"])
def list_user_events():

    if g.user:
        user = User.query.get_or_404(session[CURR_USER_KEY])
        events = UserActivity.query.filter(UserActivity.user_id == session[CURR_USER_KEY]).all()

        return render_template('activity-view.html', user=user, events=events)
    
    else:
        return render_template('index-anon.html')


@app.route('/edit-activity/<int:event_id>', methods=["GET", "POST"])
def edit_event(event_id):

    if not g.user:
        flash("Access unauthorized. Please login.", "error")
        return redirect("/")

    event = UserActivity.query.filter(UserActivity.id == event_id).first()
    if event.activity_id == "Clothing Purchase":
        form = MoneyEventForm(obj=event)
        if form.validate_on_submit():
            emission_factor_id = "consumer_goods-type_clothing"
            param1_label = "money"
            param1_data = float(form.spend_qty.data)
            param2_label = "money_unit"
            param2_data = "usd"
            payload = format_payload(emission_factor_id, param1_label, param1_data, param2_label, param2_data)
            r = requests.post(base_url + "/estimate", data=json.dumps(payload), headers=HEADERS)
            co2_e = r.json()["co2e"]

            event.date = form.date.data
            event.spend_qty = form.spend_qty.data
            event.co2e = co2_e

            db.session.commit()
            return redirect('/view-history')

    elif event.activity_id == "Driving":
        form = DistanceEventForm(obj=event)
        if form.validate_on_submit():
            emission_factor_id = "passenger_vehicle-vehicle_type_motorcycle-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na"
            param1_label = "distance"
            param1_data = float(form.spend_qty.data)
            param2_label = "distance_unit"
            param2_data = "mi"
            payload = format_payload(emission_factor_id, param1_label, param1_data, param2_label, param2_data)
            r = requests.post(base_url + "/estimate", data=json.dumps(payload), headers=HEADERS)
            co2_e = r.json()["co2e"]

            event.date = form.date.data
            event.spend_qty = form.spend_qty.data
            event.co2e = co2_e

            db.session.commit()
            return redirect('/view-history')

    elif event.activity_id == "Plastic Bottle Purchase":
        form = MoneyEventForm(obj=event)
        if form.validate_on_submit():
            emission_factor_id = "consumer_goods-type_soft_drinks_bottled_water_ice"
            param1_label = "money"
            param1_data = float(form.spend_qty.data)
            param2_label = "money_unit"
            param2_data = "usd"
            payload = format_payload(emission_factor_id, param1_label, param1_data, param2_label, param2_data)
            r = requests.post(base_url + "/estimate", data=json.dumps(payload), headers=HEADERS)
            co2_e = r.json()["co2e"]

            event.date = form.date.data
            event.spend_qty = form.spend_qty.data
            event.co2e = co2_e

            db.session.commit()
            return redirect('/view-history')

    elif event.activity_id == "Flying":
        form = AirTravelEventForm(obj=event)
        if form.validate_on_submit():
            event.date = form.date.data
            event.IATA_from = form.start_airport.data
            event.IATA_to = form.land_airport.data

            db.session.commit()
            return redirect('/view-history')

    return render_template('activity-edit.html', form=form, event=event)


@app.route('/delete-activity/<int:user_activity_id>', methods=["POST"])
def delete_event(user_activity_id):

    event = UserActivity.query.get_or_404(user_activity_id)

    db.session.delete(event)
    db.session.commit()

    return redirect('/view-history')

