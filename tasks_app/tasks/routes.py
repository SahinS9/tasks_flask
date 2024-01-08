from flask import Blueprint
from flask_login import login_required
from tasks_app.tasks.forms import TaskForm

tasks = Blueprint('tasks',__name__)

@tasks.route('/task/new')
@login_required


@tasks.route('/task/<int:task_id>')
@login_required
def edit_task():
    pass

@task.route('/task/<int:task_id>/delete', methods = ['POST'])
@login_required




