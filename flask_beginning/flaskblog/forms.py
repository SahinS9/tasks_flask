from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


from flask_wtf.file import FileField, FileAllowed #for updating profile picture in this case


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    #validation for registration error
    def validate_username(self, username):

        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username taken! Please choose different one! ')

    def validate_email(self, email):

        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email is used! Use another email!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AccountForm(FlaskForm):
    username = StringField('Username',validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators = [DataRequired(),Email()])
    picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    #user should be able to click submit without change - but we should not get error as "it s already taken"

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError(f'{user.username} is already taken! Please, change to another one!')


    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError(f'{user.email} is already used! Please, choose different email!')

    












