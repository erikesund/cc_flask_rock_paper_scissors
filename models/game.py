from models.player import Player

player_1 = Player("Erik", "rock")
player_2 = Player("Derek", "paper")

players = [player_1, player_2]

def get_players():
    return players

def determine_winner():
        if player_1.guess == player_2.guess:
            return None
        elif player_1.guess == "rock" and player_2.guess == "scissors":
            return player_1
        elif player_1.guess == "rock" and player_2.guess == "paper":
            return player_2
        elif player_1.guess == "paper" and player_2.guess == "rock":
            return player_1
        elif player_1.guess == "paper" and player_2.guess == "scissors":
            return player_2
        elif player_1.guess == "scissors" and player_2.guess == "paper":
            return player_1
        elif player_1.guess == "scissors" and player_2.guess == "rock":
            return player_2
        
