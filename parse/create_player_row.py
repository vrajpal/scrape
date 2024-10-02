from PlayerController import PlayerController
from models.Player import Player
from utils import batting
from dotenv import dotenv_values

config = dotenv_values(".env")


def create_player(row, position):
    player_controller = PlayerController()
    player_row = {}
    name = row.find("td", {"data-stat": "player"}).contents[0].text
    for stat in batting:
        value = row.find("td", {"data-stat": stat}).contents
        player_row[stat] = value
    print(name)
    name_holder = name.split()
    age = row.find("td", {"data-stat": "age"}).contents
    if name_holder:
        # need to figure out how to pass team id
        player = Player(name_holder[0], name_holder[1], age, 1, position)
        print(player)
        player_controller.create_player(player)
