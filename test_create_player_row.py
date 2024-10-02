from models.Player import Player
from parse.create_player_row import create_player


with open("./test_output.txt", 'r') as file:
    rows = file.read()

print(rows)

test_player = Player("testy", "mctesterson", 23, 25, "1B")
create_player(test_player, "1B")
