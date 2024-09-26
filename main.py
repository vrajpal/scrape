"""requests libray to pull down baseball ref"""

import requests
from dotenv import dotenv_values
from models.Player import Player
from PlayerController import PlayerController
from db import Session
from parse.soup_the_page import soup_the_page
from parse.team_batting import all_team_batting
from utils import batting

session = Session()

config = dotenv_values(".env")
player_controller = PlayerController(session)

print(config)
# grab html of the mariners season page
page = requests.get(
    f"https://www.baseball-reference.com/teams/{config['TEAM']}/{config['SEASON_YEAR']}.shtml",
    timeout=10,
)

# convert html into bs objects
soup = soup_the_page(page)
# grab table with hitting stats and return list of rows
rows = all_team_batting(soup)

########################EXTRACT#########################################


# given a row in the hitting table, find each batting stat and save to a dictionary
def create_player_stats(row):
    """
    Extracts player statistics from an HTML row element and creates a Player object.

    Args:
        row (BeautifulSoup Tag): A BeautifulSoup Tag object representing a table row containing player data.

    Returns:
        None

    This function performs the following steps:
    1. Extracts the player's name from the row.
    2. Iterates over a predefined list of batting statistics, extracting each stat's value from the row.
    3. Prints the player's name.
    4. Splits the player's name into first and last names.
    5. Extracts the player's age from the row.
    6. Extracts the player's position from the row.
    7. Creates a Player object using the extracted data.
    8. Prints the Player object.
    9. Calls a method to create the player in the player controller.
    10. Prints the Player object again.
    """
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


################################################################################################


# for each player in the batting table, parse it
for row in rows:
    # find the data cell with player in it
    breakpoint()
    positionRow = row.find("td", {"data-stat": "pos"})
    if positionRow != None:
        position = positionRow.contents[0].text
        # if the player is not a pitcher, process it
        if position != "P" and position != None:
            # print("Position: ")
            # print(position)
            create_player_stats(row)
