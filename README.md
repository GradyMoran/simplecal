# simplecal
A simple online shared calendar with no authentication

sudo pip3 install -r requirements.txt

something about creating db and applying schema? not sure what command this is

https://github.com/GradyMoran/simplecal

TODO (rougly in order):
edit/delete events

time of day support

change calendar ID from int to string type

securify/robustify

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
