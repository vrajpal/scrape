from models import Player
from utils import batting

def create_player_stats(row, player_controller):
    player_row = {}
    name = row.find("td", {"data-stat": "player"}).contents[0].text
    for stat in batting:
        value = row.find("td", {"data-stat": stat}).contents
        player_row[stat] = value
    print(name)
    name_holder = name.split()
    age = row.find("td", {"data-stat": "age"}).contents 
    position = positionRow.contents[0].text
    if name_holder:
        player = Player(name_holder[0], name_holder[1], age, 1, position)
        print(player)
        player_controller.create_player(player)
        print(player)
