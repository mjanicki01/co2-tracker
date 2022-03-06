from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()



def connect_db(app):
    db.app = app
    db.init_app(app)


class Activity(db.Model):
    """Snapshot record of activities used from Climatiq API"""

    __tablename__ = "activity"
      
    id = db.Column(db.String(8),
                    primary_key=True)
    emission_factor_id = db.Column(db.String, nullable=False, unique=True)
    spend_unit = db.Column(db.String(6), nullable=False) #rename to params?
    co2e = db.Column(db.Float, nullable=False)
    activities = db.relationship('UserActivity', backref='activity', viewonly=True)


class User(db.Model):

    __tablename__ = "users"
      
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False) #revise
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    #location
    #modeoftransport
    events = db.relationship('Event', secondary='user_activity', backref='users', viewonly=True)

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


class Event(db.Model):
    """ Join table connecting users & user activity history"""

    __tablename__ = "event"

    user_id = db.Column(db.Integer, db.ForeignKey(
            'users.id'), primary_key=True)
    user_activity_id = db.Column(db.Integer, db.ForeignKey(
            'user_activity.id'), primary_key=True)
    events = db.relationship('UserActivity', backref='event', viewonly=True)


class UserActivity(db.Model):
    """ Individual user activities """

    __tablename__ = "user_activity"
      
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,
                    db.ForeignKey('users.id', ondelete='cascade'))
    emission_factor_id = db.Column(db.String,
                    db.ForeignKey('activity.emission_factor_id', ondelete='cascade'))
    date = db.Column(db.Date, nullable=False)
    leg_1 = db.Column(db.String(4), nullable=True)
    leg_2 = db.Column(db.String(4), nullable=True)
    spend_qty = db.Column(db.Float)
    spend_unit = db.Column(db.String(6), nullable=False)
    co2e = db.Column(db.Float, nullable=False)
    users = db.relationship('User', backref='user_activity', viewonly=True)
    activity_data = db.relationship('Activity', backref='user_activity', viewonly=True)


# todo: add comments object:
#    comment PK
#    comment string
#    comment FK relationship -> event PK


