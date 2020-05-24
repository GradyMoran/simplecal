#This object is what is stored in the database.
from datetime import datetime
from db import db
from itertools import combinations
from random import randint, shuffle

class CalData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
