from app import create_app, db
from app.models import User, Task, Note

# Create the Flask app instance
app = create_app()

# Set up the app context and create the database tables
with app.app_context():
    db.create_all()
