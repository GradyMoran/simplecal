from flask_sqlalchemy import SQLAlchemy

db = None

def init_db(app):
    global db
    db = SQLAlchemy(app)

def get_db():
    return db