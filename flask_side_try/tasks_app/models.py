from tasks_app import db



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    password = db.Column(db.String, nullable=False)
    tasks = db.relationship('UserTask', backref='user', lazy=True, cascade = 'save-update, merge, refresh-expire, expunge')

    def __repr__(self):
        return f"User {self.id}: {self.username} - {self.email}"

class UserTask(db.Model):
    __tablename__ = 'user_tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    desc = db.Column(db.String(150), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    tags = db.relationship('TaskTag', backref = 'task', lazy=True, cascade = 'save-update, merge, refresh-expire, expunge')

    def __repr__(self):
        return f"Task: {self.id} - {self.name} by {self.user_id}"

class TaskTag(db.Model):
    __tablename__ = 'task_tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    desc = db.Column(db.String(80))

    task_id = db.Column(db.Integer, db.ForeignKey('user_tasks.id'), nullable=True)

    def __repr__(self):
        return f"Tag: {self.id} - {self.name}"