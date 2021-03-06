from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, PasswordField, DateField, TextAreaField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, Email, Length, NumberRange, DataRequired, ValidationError
from models import User


"""User Forms"""

def validate_credentials(form, field):

    username = form.username.data
    password = field.data

    user = User.query.filter_by(username=username).first()
    if user is None:
        raise ValidationError('Username does not exist')
    elif User.authenticate(username, password) == False:
        raise ValidationError('Password is incorrect')


class LoginForm(FlaskForm):

    username = StringField('Username',
        validators=[InputRequired(message="Username required"), Length(min=5, max=20)])
    password = PasswordField('Password',
        validators=[InputRequired(message="Password required"), Length(min=6, max=55), validate_credentials])


class RegisterForm(FlaskForm):

    username = StringField('Username',
        validators=[InputRequired(), Length(min=5, max=20)])
    email = StringField('Email',
        validators=[DataRequired(), Email(), Length(max=50)])
    first_name = StringField('First Name',
        validators=[InputRequired(), Length(max=30)])
    last_name = StringField('Last Name',
        validators=[InputRequired(), Length(max=30)])
    password = PasswordField('Password',
        validators=[InputRequired(), Length(min=6, max=55)])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already in use')



class EditProfileForm(FlaskForm):

    username = StringField('Username',
        validators=[DataRequired()])
    email = StringField('Email',
        validators=[DataRequired(), Email()])
    first_name = StringField('First Name',
        validators=[InputRequired(), Length(max=30)])
    last_name = StringField('Last Name',
        validators=[InputRequired(), Length(max=30)])
    image_url = StringField('Image URL')
    location = StringField('Location')
    mode_of_transport = SelectField('Primary Mode of Transportation',
        choices=[('Walking', 'Walking'), 
                ('Bicycle', 'Bicycle'), 
                ('Car (gas)', 'Car (gas)'),
                ('Car (hybrid)', 'Car (hybrid)'),
                ('Car (ev)', 'Car (ev)'),
                ('Motorcycle', 'Motorcycle'),
                ('Teleportation', 'Teleportation'),
                ('Horseback', 'Horseback'),
                ('Broomstick', 'Broomstick'),
                ('Palanquin', 'Palanquin')])
    password = PasswordField('Password',
        validators=[InputRequired(), Length(min=6, max=55)])


"""Activity Forms - Add & Edit"""

class MoneyEventForm(FlaskForm):

    user_id = IntegerField('user_id', default=1)
    date = DateField('Date',
        validators=[DataRequired()])
    spend_qty = DecimalField('Total Purchase ($ USD)',
        validators=[InputRequired()])


class DistanceEventForm(FlaskForm):

    user_id = IntegerField('user_id', default=1)
    date = DateField('Date',
        validators=[DataRequired()])
    spend_qty = DecimalField('Miles',
        validators=[InputRequired()])


class AirTravelEventForm(FlaskForm):

    user_id = IntegerField('user_id', default=1)
    date = DateField('Date',
        validators=[DataRequired()])
    start_airport = StringField('Take-off Airport')
    land_airport = StringField('Landing Airport')        


class AddCommentForm(FlaskForm):
#add comment to event
    pass