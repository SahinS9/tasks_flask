from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class RegistrationForm():
    id = "a"


class LoginForm():
    id = 'a'

class TagForm():
    id = 'a'

class TaskForm(FlaskForm):
    name = StringField('Task Name', validators=[DataRequired(), Length(max=20)])
    desc = TextAreaField('Description')
    finished_at = DateField('Deadline', format='%Y-%m-%d', validators=[DataRequired()])


