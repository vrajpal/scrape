import requests
from dotenv import dotenv_values
from models.Player import Player
from PlayerController import PlayerController
from db import Session
from parse.soup_the_page import soupThePage
from parse.team_batting import all_team_batting
session = Session()

config = dotenv_values(".env") 
player_controller = PlayerController(session)

print(config)
# grab html of the mariners season page
page = requests.get(f"https://www.baseball-reference.com/teams/{config['TEAM']}/{config['SEASON_YEAR']}.shtml")

# convert html into bs objects
soup = soupThePage(page)
# grab table with hitting stats and return list of rows 
rows = all_team_batting(soup)

# the headers for the batting table in Baseball Ref, remove player as its method for grabbing name is inconsistent 
batting = {"age", "G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SB", 
           "CS", "BB", "SO", "batting_avg", "onbase_perc", "slugging_perc", "onbase_plus_slugging", 
           "onbase_plus_slugging_plus", "TB", "GIDP", "HBP", "SH", "SF", "IBB"}

# given a row in the hitting table, find each batting stat and save to a dictionary
def create_player_stats(row):
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

# for each player in the batting table, parse it
for row in rows:
    # find the data cell with player in it 
    breakpoint()
    positionRow = row.find("td", {"data-stat": "pos"})
    if(positionRow != None):
        position = positionRow.contents[0].text
        # if the player is not a pitcher, process it
        if position != 'P' and position != None:
            # print("Position: ")
            # print(position)
            create_player_stats(row) 

