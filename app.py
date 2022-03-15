from flask import Flask, render_template, flash, redirect, session, g, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddMoneyEventForm, AddAirTravelEventForm, AddDistanceEventForm, RegisterForm, LoginForm
from models import db, connect_db, User, Activity, UserActivity, Event
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///co2budget"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)

db.create_all()
db.session.commit()


##################################################################################################
"""General"""


CURR_USER_KEY = "curr_user"

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
        events = Event.query.all()
        return render_template('index.html', events=events)

    else:
        return render_template('index-anon.html')


##################################################################################################
""" User Sign-up, Sign-in, & Logout"""


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


##################################################################################################
"""Add, Edit, View, & Delete User Activities"""

@app.route('/add-activity', methods=["GET"])
def form():
    
    form_money = AddMoneyEventForm()
    form_distance = AddDistanceEventForm()
    form_air_travel = AddAirTravelEventForm()

    return render_template('activity-add.html',
        form_money=form_money,
        form_distance=form_distance,
        form_air_travel=form_air_travel)


@app.route('/post-activity', methods=["POST"])
def add_new_event():
    
    newevent = UserActivity(
    user_id = request.json["user_id"], #doesn't need to be pulled in from the form
    activity_id = request.json["activity_id"],
    emission_factor_id = request.json["e_id"],
    date = request.json["date"],
    IATA_from = request.json["from"] or None,
    IATA_to = request.json["to"] or None,
    spend_qty = request.json["spend_qty"] or None,
    spend_unit = request.json["spend_unit"] or None,
    co2e = request.json["co2e"]
    )

    db.session.add(newevent)
    db.session.commit()

    return redirect('/')


@app.route('/view-history/<int:user_id>', methods=["GET"]) #remove query
def list_user_events(user_id):

    user = User.query.get_or_404(user_id)
    events = UserActivity.query.filter(UserActivity.user_id == user_id).all()

    return render_template('activity-view.html', user=user, events=events)
    

@app.route('/edit-activity/<int:user_activity_id>', methods=["POST"])
def edit_event():

    return render_template('activity-view.html')


@app.route('/delete-activity/<int:user_activity_id>', methods=["POST"])
def delete_event(user_activity_id):

    event = UserActivity.query.get_or_404(user_activity_id)

    db.session.delete(event)
    db.session.commit()

    return redirect('/view-history')
