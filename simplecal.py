#need to cite https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world , I am using first five tutorials heavily
from enum import Enum
from random import randint

from flask import Flask
from flask import render_template, flash, redirect, request, session, url_for
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import or_

from db import get_db, init_db
from forms import TestForm

app = Flask(__name__)
#the following line "creates a token that is used to protect against csrf attacks".
# Should learn what it does and include in report... I'm just following a tutorial.
app.config['SECRET_KEY'] = 'change-me' #probably want to do an environment variable

#probably want to set this to an environment variable too
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////var/www/simplecal/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

csrf = CSRFProtect()
csrf.init_app(app)

init_db(app)

# These models have to be imported after the database connection is initialized
from models import CalData

@app.route('/')
def simplecal_home():
    return render_template('home.html', title='Home')

@app.route('/calendar/<calendar_id>', methods=['GET', 'POST'])
def calendar(calendar_id):
    # Make sure the game ID is numeric and greater than zero
#    try:
#        game_id_int = int(game_id)
#        if game_id_int < 0:
#            return ('Page not found', 404)
#    except ValueError:
#        return ('Page not found', 404)
#
#    g = Game.query.filter_by(id=game_id).first()
#    if g is None:
#        return ('Page not found', 404)

#    return render_template('gameplay.html',
#                       game_id=game_id,
#                       phase=g.phase,
#                       count=g.count,
#                       player_one=player_one.username,
#                       player_two=player_two.username,
#                       dealer=dealer,
#                       player_cards=player_cards,
#                       opponent_card_count=opponent_card_count,
#                       crib_card_count=crib_card_count,
#                       played_cards=g.get_played_cards(),
#                       starter_card=g.card_to_obj(g.starter_card),
#                       player_score=player_score,
#                       opponent_score=opponent_score,
#                       player_one_score=g.player_one_score,
#                       player_two_score=g.player_two_score,
#                       is_player_turn=is_player_turn,
#                       is_ongoing=g.is_ongoing,
#                       actions=actions)

    return ('Calendar with id: ' + str(calendar_id))

    #csrf.protect() #??

    #get_db().session.commit() #will have to do stuff like this

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
