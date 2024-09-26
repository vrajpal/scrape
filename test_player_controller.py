from PlayerController import PlayerController
from models.Player import Player


test_player = Player("testy", "mctesterson", 25, 25, "C")


player_controller = PlayerController()

player_controller.create_player(test_player)
