# simplecal
A simple online shared calendar with no authentication

sudo pip3 install -r requirements.txt

https://github.com/GradyMoran/simplecal

TODO (rougly in order):
Add other plugins to the calendar

Find how to pass calendar data to the calendar when you load it. Should happen on python side

how to pass new calendar entries to python?

Save/load from database
    (how to do prepared statements here?)
    (how to prevent someone putting javascript in the calendar entries?)
    
prettify

deploy on azure (should code be public?)

encrypt calendars in db. WIP scheme is the url for the calendar is 32 characters, first 8 characters are primary key in db to locate a binary chunk of data that can be decrypted with other 24 characters from url.

other security thoughts:
xss (server-side form validation? not sure), csrf (flask token), and sql injection (prepared statements? could be complex) are all on the table for this site
need rate limiting
calendar size limit
if we go with above encryption scheme may want some lag timer added on to the "failed to find calendar" message so a user can't brute force first 8 chars to find where calendars are located. but this is probably not worth the effort with proper rate limiting
