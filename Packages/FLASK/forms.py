from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

## importing data required to require a field, and length to set length req, and check if email is valid, and equal to for matching password to confirm password
## forms for registration and user generation
##importing module to help create username attribute and password to help create a PW, and submitfield to submit the data, boolean to remember pw for sometime



class RegistrationForm(FlaskForm): ## creating a registration class that will import from FlaskForm we imported
    username = StringField('Username',validators=[DataRequired(),Length(min=1,max=20)])## creating username attribute with Username as tag for HTML and validators to limit what can be a username(required and length)
    email = StringField('Email',validators=[DataRequired(),Email()]) ##making sure email is valid
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm): ## creating a login class that will import from FlaskForm we imported
    email = StringField('Email',validators=[DataRequired(),Email()]) ##making sure email is valid
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')