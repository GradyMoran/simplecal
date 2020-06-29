#Mega thanks to https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
import os

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
    cal = CalData.query.get_or_404(int(calendar_id))
    return render_template("calendar.html", calendarId=calendar_id, events=cal.events)

    #csrf.protect() #??

@app.route('/update', methods=['POST'])
def update():
    print(str(request.form))
    return "200 OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
