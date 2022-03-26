from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

bcrypt = Bcrypt()
db = SQLAlchemy()



def connect_db(app):
    db.app = app
    db.init_app(app)



class User(db.Model):

    __tablename__ = "users"
      
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    username = db.Column(db.String(20),
                    nullable=False,
                    unique=True)
    email = db.Column(db.String(50),
                    nullable=False,
                    unique=True)
    password = db.Column(db.String,
                    nullable=False)
    first_name = db.Column(db.String(30),
                    nullable=False)
    last_name = db.Column(db.String(30),
                    nullable=False)
    image_url = db.Column(db.Text, default="/static/images/user.png")
    location = db.Column(db.String(200))
    mode_of_transport = db.Column(db.String(200))

    @classmethod
    def register(cls, username, password, first_name, last_name, email):

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        user = cls(
            username=username,
            password=hashed_utf8,
            first_name=first_name,
            last_name=last_name,
            email=email)

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False



class UserActivity(db.Model):
    """ Individual user activities """

    __tablename__ = "user_activity"
      
    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    user_id = db.Column(db.Integer,
                    db.ForeignKey('users.id',
                    ondelete='cascade'))
    activity_id = db.Column(db.String(40),
                    nullable=False)
    emission_factor_id = db.Column(db.String)
    date = db.Column(db.Date,
                    nullable=False)
    IATA_from = db.Column(db.String(4))
    IATA_to = db.Column(db.String(4))
    spend_qty = db.Column(db.Float)
    spend_unit = db.Column(db.String(10))
    co2e = db.Column(db.Float,
                    nullable=False)
    users = db.relationship('User',
                    backref='user_activity',
                    viewonly=True)

    def sum_all(user_id):
        sum_co2e = 0
        sum_co2e_curr_month = 0
        sum_co2e_curr_year = 0
        user_total_activities = UserActivity.query.filter_by(user_id=user_id).all()
        for activity in user_total_activities:
            sum_co2e = sum_co2e + activity.co2e
            if str(datetime.now().year) in str(activity.date):
                sum_co2e_curr_year = sum_co2e_curr_year + activity.co2e
                if str(datetime.now().month) in str(activity.date):
                    sum_co2e_curr_month = sum_co2e_curr_month + activity.co2e

        return [round(sum_co2e),
                round(sum_co2e_curr_month),
                round(sum_co2e_curr_year)]

    def sum_all_flights(user_id):
        sum_co2e = 0
        sum_co2e_curr_month = 0
        sum_co2e_curr_year = 0
        user_total_activities = UserActivity.query.filter_by(user_id=user_id).all()
        for activity in user_total_activities:
            if "Flying" in activity.activity_id:
                sum_co2e = sum_co2e + activity.co2e
                if str(datetime.now().year) in str(activity.date):
                    sum_co2e_curr_year = sum_co2e_curr_year + activity.co2e
                    if str(datetime.now().month) in str(activity.date):
                        sum_co2e_curr_month = sum_co2e_curr_month + activity.co2e

        return [round(sum_co2e),
                round(sum_co2e_curr_month),
                round(sum_co2e_curr_year)]

    def sum_all_drives(user_id):
        sum_co2e = 0
        sum_miles = 0
        sum_co2e_curr_month = 0
        sum_miles_curr_month = 0
        sum_co2e_curr_year = 0
        sum_miles_curr_year = 0
        user_total_activities = UserActivity.query.filter_by(user_id=user_id).all()
        for activity in user_total_activities:
            if "Driving" in activity.activity_id:
                sum_co2e = sum_co2e + activity.co2e
                sum_miles = sum_miles + activity.spend_qty
                if str(datetime.now().year) in str(activity.date):
                    sum_co2e_curr_year = sum_co2e_curr_year + activity.co2e
                    sum_miles_curr_year = sum_miles_curr_year + activity.spend_qty
                    if str(datetime.now().month) in str(activity.date):
                        sum_co2e_curr_month = sum_co2e_curr_month + activity.co2e
                        sum_miles_curr_month = sum_miles_curr_month + activity.spend_qty

        return [round(sum_co2e),
                round(sum_miles),
                round(sum_co2e_curr_month),
                round(sum_miles_curr_month),
                round(sum_co2e_curr_year),
                round(sum_miles_curr_year)]

    def sum_all_clothing(user_id):
        sum_co2e = 0
        sum_money = 0
        sum_co2e_curr_month = 0
        sum_money_curr_month = 0
        sum_co2e_curr_year = 0
        sum_money_curr_year = 0
        user_total_activities = UserActivity.query.filter_by(user_id=user_id).all()
        for activity in user_total_activities:
            if "Clothing" in activity.activity_id:
                sum_co2e = sum_co2e + activity.co2e
                sum_money = sum_money + activity.spend_qty
                if str(datetime.now().year) in str(activity.date):
                    sum_co2e_curr_year = sum_co2e_curr_year + activity.co2e
                    sum_money_curr_year = sum_money_curr_year + activity.spend_qty
                    if str(datetime.now().month) in str(activity.date):
                        sum_co2e_curr_month = sum_co2e_curr_month + activity.co2e
                        sum_money_curr_month = sum_money_curr_month + activity.spend_qty

        return [round(sum_co2e),
                round(sum_money, 2),
                round(sum_co2e_curr_month),
                round(sum_money_curr_month, 2),
                round(sum_co2e_curr_year),
                round(sum_money_curr_year, 2)]

    def sum_all_bottles(user_id):
        sum_co2e = 0
        sum_money = 0
        sum_co2e_curr_month = 0
        sum_money_curr_month = 0
        sum_co2e_curr_year = 0
        sum_money_curr_year = 0
        user_total_activities = UserActivity.query.filter_by(user_id=user_id).all()
        for activity in user_total_activities:
            if "Bottle" in activity.activity_id:
                sum_co2e = sum_co2e + activity.co2e
                sum_money = sum_money + activity.spend_qty
                if str(datetime.now().year) in str(activity.date):
                    sum_co2e_curr_year = sum_co2e_curr_year + activity.co2e
                    sum_money_curr_year = sum_money_curr_year + activity.spend_qty
                    if str(datetime.now().month) in str(activity.date):
                        sum_co2e_curr_month = sum_co2e_curr_month + activity.co2e
                        sum_money_curr_month = sum_money_curr_month + activity.spend_qty

        return [round(sum_co2e),
                round(sum_money, 2),
                round(sum_co2e_curr_month),
                round(sum_money_curr_month, 2),
                round(sum_co2e_curr_year),
                round(sum_money_curr_year, 2)]






# todo: add comments object:
#    comment PK
#    comment string
#    comment FK relationship -> event PK


