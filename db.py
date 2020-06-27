from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = None
migrate = None

def init_db(app):
    global db
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

def get_db():
    return db

def get_migrate():
    return migrate
