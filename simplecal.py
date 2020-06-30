#Mega thanks to https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
import datetime
import os
import random
import string

from flask import Flask
from flask import render_template, flash, redirect, request, session, url_for, send_from_directory
from flask_wtf.csrf import CSRFProtect
#why is this sqlalchemy, not flask_sqlalchemy?
from sqlalchemy import or_
from flask_migrate import Migrate

from db import get_db, init_db, get_migrate

app = Flask(__name__, static_url_path='')
#the following line "creates a token that is used to protect against csrf attacks".
# Should learn what it does and include in report... I'm just following a tutorial.
#app.config['SECRET_KEY'] = 'change-me' #probably want to do an environment variable

#probably want to set this to an environment variable too
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#csrf = CSRFProtect()
#csrf.init_app(app)

init_db(app)

# These models have to be imported after the database connection is initialized
from models import CalData, Event

#TODO: when this is deployed on a real web server, need to change this part as well as some config in the web server integration to make the web server give these pages instead of going through flask. This is a workaround to use the flask dev server. This method should be removed when deployed. https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
@app.route('/calendar/fullcalendar/<path:path>')
def send_fc(path):
    return send_from_directory('fullcalendar', path)

@app.route('/')
def simplecal_home():
    return render_template('home.html', title='Home')

#POST not needed here. Conceptually, how new events get added/removed from the calender database is there needs to be a javascript function invoked when the user modifies/adds/deletes an event (how?) that makes a post request to the server with the data for that event, somehow. I do not want a "save" button.
@app.route('/calendar/<calendar_id>', methods=['GET'])
def calendar(calendar_id):
    cal = CalData.query.get_or_404(calendar_id)
    return render_template("calendar.html", calendarId=calendar_id, events=cal.events)

    #csrf.protect() #??

@app.route('/new', methods=['GET'])
def new_calendar():
    cal_id_len = 64
    id_gen_tries = 10
    tries = 0
    letters = string.ascii_letters + string.digits
    tmp_id = ''.join([random.choice(letters) for i in range(0, cal_id_len)])
    while((CalData.query.get(tmp_id) is not None) and (tries < id_gen_tries)):
        tries += 1
        tmp_id = ''.join([random.choice(letters) for i in range(0, cal_id_len)])
    if tries >= id_gen_tries:
        return "400"
    new_cal = CalData(id=tmp_id)
    conn = get_db()
    conn.session.add(new_cal)
    conn.session.commit()
    return redirect("/calendar/" + tmp_id)

#TODO: error handling, etc
#May want to separate into update/delete/edit functionalities, or else we'll need a separate parameter to determine what to do, or something weird.
@app.route('/update', methods=['POST'])
def update():
    print(str(request.form))
    #check if request.form?
    #'Mon Jun 22 2020 00:00:00 GMT-0400 (Eastern Daylight Time)'
    #may break if user-side locale differs from server-side. consider different format?
    start_str = request.form["start"].split("(")[0].strip()
    #print("start_str: " + start_str)
    start_dt = datetime.datetime.strptime(start_str, "%a %b %d %Y %H:%M:%S GMT%z")
    #print("start_dt: " + str(start_dt))
    end_str = request.form["end"].split("(")[0].strip()
    end_dt = datetime.datetime.strptime(end_str, "%a %b %d %Y %H:%M:%S GMT%z")
    event = Event(start=start_dt, end=end_dt, title=request.form["title"], caldata=CalData.query.get_or_404(request.form["calendarId"]))
    conn = get_db()
    conn.session.add(event)
    conn.session.commit()
    return "200 OK" #??

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
