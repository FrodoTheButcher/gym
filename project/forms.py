from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , IntegerField , FloatField,SelectField
from wtforms.validators import DataRequired , Email , EqualTo
from wtforms import ValidationError
from .models import User

class Level(FlaskForm):
    beginner=SelectField("Beginner")
    intermediate=SelectField("Intermediate")
    advanced=SelectField("Advanced")

class Calculator(FlaskForm):
    weight=IntegerField('Weight',validators=[DataRequired()])
    height=IntegerField('Height',validators=[DataRequired()])
    age=IntegerField('Age',validators=[DataRequired()])
    submit=SubmitField('Calculate!')
class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm')])
    pass_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registerd!')
    
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username taken!')

    

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')