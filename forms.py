from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, DateField, TextAreaField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, Email, Length, NumberRange, DataRequired


"""User Forms"""

class LoginForm(FlaskForm):

    username = StringField('Username',
        validators=[InputRequired(), Length(min=5, max=20)])
    password = PasswordField('Password',
        validators=[InputRequired(), Length(min=6, max=55)])


class RegisterForm(FlaskForm):

    username = StringField('Username',
        validators=[InputRequired(), Length(min=5, max=20)])
    email = StringField('Email',
        validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField('Password',
        validators=[InputRequired(), Length(min=6, max=55)])
    first_name = StringField('First Name',
        validators=[InputRequired(), Length(max=20)])
    last_name = StringField('Last Name',
        validators=[InputRequired(), Length(max=20)])


class EditProfileForm(FlaskForm):

    username = StringField('Username',
        validators=[DataRequired()]) #review datarequired vs input-required - interchangeable?
    email = StringField('Email',
        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
        validators=[InputRequired(), Length(min=6, max=55)]) #turn off inputrequired?
    first_name = StringField('First Name',
        validators=[InputRequired(), Length(max=20)])
    last_name = StringField('Last Name',
        validators=[InputRequired(), Length(max=20)])
    #image_url = StringField('Image URL')
    #location = ...
    #primary mode of transport = SelectField('...',
        #choices=[('Walking' - 100%, 'Cat'),  ('Cycling' - 100%, 'Dog'),  ('Car (gas)' - 0%, 'Porcupine'),
        # ('Motorcycle' - 25%, 'Porcupine')]), ('Broomstick' - 100%, 'Porcupine')], ('Teleportation' - 100%, 'Porcupine')]
        # add avatar next to profile image


"""Activity Forms - Add"""

class AddMoneyEventForm(FlaskForm):

    user_id = IntegerField('user_id', default=1)
    date = DateField('Date',
        validators=[DataRequired()])
    spend_qty = FloatField('Qty',
        validators=[InputRequired()])
#include USD & Title of activity type in HTML


class AddDistanceEventForm(FlaskForm):

    user_id = IntegerField('user_id', default=1)
    date = DateField('Date',
        validators=[DataRequired()])
    spend_qty = FloatField('Qty',
        validators=[InputRequired()])


class AddAirTravelEventForm(FlaskForm):

    user_id = IntegerField('user_id', default=1)
    date = DateField('Date',
        validators=[DataRequired()])
    start_airport = StringField('Take-off Airport')
    land_airport = StringField('Landing Airport')        
   

class EditActivityForm(FlaskForm):

    pass


class AddCommentForm(FlaskForm):
#add comment to event
    pass