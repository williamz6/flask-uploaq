from flaskupload import app, mysql
from wtforms import SubmitField, StringField, TextAreaField, PasswordField, validators, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_wtf import FlaskForm, form
from flaskupload.models import User


# registration form class
class RegForm(FlaskForm):
    first_name= StringField('First Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])
    username= StringField('Username',[validators.length(min=5, max=15)])
    email = StringField('Email',
     [validators.Email(),
      validators.DataRequired(), 
      validators.Length(min=6, max=35)])
    password = PasswordField('New Password', 
    [validators.DataRequired(), 
    validators.Length(min=3), 
    validators.EqualTo('confirm_pass', message='Passwords must match')])
    confirm_pass=PasswordField('Confirm Password')
    submit= SubmitField('Sign Up')

    def validate_username(self, username):
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError(f'{username.data} is already taken')

    
    def validate_email(self, email):
      user = User.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError(f'Email already taken by registered user')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

