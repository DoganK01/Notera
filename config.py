import os

class Config:
    SECRET_KEY = os.urandom(24)  # For session management and CSRF protection
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # SQLite database for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
