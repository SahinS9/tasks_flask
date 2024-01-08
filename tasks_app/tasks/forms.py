from flask import FlaskForm
from wtforms import StringField, TextAreaField, SubmitFieldf
from wtform.validators import DataRequired

class TaskForm(FlaskForm):
    name = StringField('name', validators = [DataRequired()])
    deadline = DateField('deadline', validators=[])
    submit = SubmitField('Task')

