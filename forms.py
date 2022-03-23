from email.policy import default
import numbers
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
    elif User.authenticate == False:
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
    password = PasswordField('Password',
        validators=[InputRequired(), Length(min=6, max=55)])
    first_name = StringField('First Name',
        validators=[InputRequired(), Length(max=20)])
    last_name = StringField('Last Name',
        validators=[InputRequired(), Length(max=20)])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')




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
    image_url = StringField('(Optional) Image URL')
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
    spend_qty = DecimalField('Qty',
        validators=[InputRequired()])


class AddDistanceEventForm(FlaskForm):

    user_id = IntegerField('user_id', default=1)
    date = DateField('Date',
        validators=[DataRequired()])
    spend_qty = DecimalField('Qty',
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