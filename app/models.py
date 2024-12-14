from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(255))
    priority = db.Column(db.String(50))
    due_date = db.Column(db.String(20))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note_title = db.Column(db.String(100), nullable=False)
    note_content = db.Column(db.String(500), nullable=False)
