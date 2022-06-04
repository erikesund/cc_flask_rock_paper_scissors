
from flask import render_template

from app import app
from models.player import Player
from models.game import *

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    return render_template("/game/index.html")

# @app.route("/players")
# def players_index():
#     players = get_players()
#     return render_template("players/index.html", players = players)

@app.route("/game/<guess1>/<guess2>")
def result(guess1, guess2):
    player_1.guess = guess1
    player_2.guess = guess2
    winning_player = determine_winner()
    return render_template("/game/results.html", winning_player=winning_player)
   