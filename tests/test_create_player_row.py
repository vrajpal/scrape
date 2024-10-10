import models.Player as Player
from parse.create_player_row import create_player


with open("./test_output.txt", 'r') as file:
    rows = file.read()

for row in rows:
    breakpoint()
    print(row)

test_player = Player("testy", "mctesterson", 23, 25, "1B")
create_player(test_player, "1B")
