from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    task_name = StringField('Task Name', validators=[DataRequired()])
    details = TextAreaField('Details')
    priority = SelectField('Priority', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    due_date = StringField('Due Date (YYYY-MM-DD)', validators=[DataRequired()])
    submit = SubmitField('Save Task')

class NoteForm(FlaskForm):
    note_title = StringField('Title', validators=[DataRequired()])
    note_content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Save Note')
