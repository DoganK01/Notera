from flask import render_template, redirect, url_for, flash, request, Blueprint
from app import db
from app.models import User, Task, Note
from app.forms import LoginForm, TaskForm, NoteForm
from werkzeug.security import check_password_hash

main = Blueprint('main', __name__)

# Login route
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

# Dashboard route
@main.route('/dashboard')
def dashboard():
    tasks = Task.query.all()
    notes = Note.query.all()
    return render_template('dashboard.html', tasks=tasks, notes=notes)

# Task creation route
@main.route('/add_task', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            task_name=form.task_name.data,
            details=form.details.data,
            priority=form.priority.data,
            due_date=form.due_date.data
        )
        db.session.add(task)
        db.session.commit()
        flash('Task Created!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('add_task.html', form=form)

# Note editing route
@main.route('/edit_note/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note = Note.query.get_or_404(id)
    form = NoteForm()
    if form.validate_on_submit():
        note.note_title = form.note_title.data
        note.note_content = form.note_content.data
        db.session.commit()
        flash('Note Updated!', 'success')
        return redirect(url_for('main.dashboard'))
    elif request.method == 'GET':
        form.note_title.data = note.note_title
        form.note_content.data = note.note_content
    return render_template('edit_note.html', form=form)
