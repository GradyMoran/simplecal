#This object is what is stored in the database.
from datetime import datetime
from db import db
from itertools import combinations
from random import randint, shuffle

class CalData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    events = db.relationship('Event', backref='caldata', lazy=True)

    def __repr__(self):
        return "ID: " + str(id)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer, unique=True)
    allDay = db.Column(db.Boolean)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    title = db.Column(db.String(256), nullable=False)
    url = db.Column(db.String(4096))
    calendar_id = db.Column(db.Integer, db.ForeignKey('cal_data.id'))

    def __repr__(self):
        return "ID: " + str(id) + \
               "groupid: " + str(groupid) + \
               "allDay: " + str(allDay) + \
               "start: " + str(start) + \
               "end: " + str(end) + \
               "title: " + str(title) + \
               "url: " + str(url)
