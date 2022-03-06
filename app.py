from flask import Flask, render_template, flash, redirect, session, g, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddMoneyEventForm, AddAirTravelEventForm, AddDistanceEventForm
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

CURR_USER_KEY = "curr_user"


@app.route('/')
def index():
    users = User.query.all()
    events = Event.query.all()
    return render_template('index.html', users=users, events=events)


@app.route('/addactivity', methods=["GET"])
def form():
    
    form_money = AddMoneyEventForm()
    form_distance = AddDistanceEventForm()
    form_air_travel = AddAirTravelEventForm()

    return render_template('activity-add.html',
        form_money=form_money,
        form_distance=form_distance,
        form_air_travel=form_air_travel)


@app.route('/postactivity', methods=["POST"])
def add_new_event():
    
    newevent = UserActivity(
    user_id = request.json["user_id"], #doesn't need to be pulled in from the form
    emission_factor_id = request.json["e_id"],
    date = request.json["date"],
    leg_1 = request.json["leg_1"] or None,
    leg_2 = request.json["leg_2"] or None,
    spend_qty = request.json["spend_qty"],
    spend_unit = request.json["spend_unit"],
    co2e = request.json["co2e"]
    )

    db.session.add(newevent)
    db.session.commit()

    return redirect('/')


# User signup/login/logout

