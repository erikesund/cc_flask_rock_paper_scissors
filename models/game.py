from models.player import Player

player_1 = Player("Erik", "Rock")
player_2 = Player("Derek", "Paper")
player_3 = Player("Scotty", "Scissors")
player_4 = Player("Adam", "Rock")

players = [player_1, player_2, player_3, player_4]

def get_players():
    return players