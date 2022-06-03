from flask import render_template

from app import app
from models.player import Player
from models.game import get_players

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    return render_template("/game/index.html")

@app.route("/players")
def players_index():
    players = get_players()
    return render_template("players/index.html", players = players)