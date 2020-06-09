# simplecal
A simple online shared calendar with no authentication

sudo pip3 install -r requirements.txt

https://github.com/GradyMoran/simplecal

TODO (rougly in order):
Calendar works when you open the html page manually, but when the site is running and you try to visit the URL, flask takes the request and sees there is no mapping for the js and css pages the html wants and returns a 404. How to let js and css and other fullcalendar/\* files requested by our pages bypass the flask routing?
Add other plugins to the calendar
Find how to pass calendar data to the calendar when you load it. Should happen on python side
how to pass new calendar entries to python?
Save/load from database
    (how to do prepared statements here?)
    (how to prevent someone putting javascript in the calendar entries?)
prettify
deploy on azure (outside the scope of this project?)
