from bs4 import BeautifulSoup
import requests
from utils import convertPositionToEnum
from dotenv import dotenv_values

config = dotenv_values(".env") 

# grab html of the mariners season page
page = requests.get(f"https://www.baseball-reference.com/teams/SEA/{config['SEASON_YEAR']}.shtml")
# convert html into bs objects
soup = BeautifulSoup(page.content, 'lxml')
# grab table with hitting stats
all_team_batting = soup.find("table", {"id": "team_batting"})
tbody = all_team_batting.find("tbody")
rows = tbody.find_all('tr')

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
    # separate the name into first name last name
    #  
    print(player_row)

# for each player in the batting table, parse it
for row in rows:
    # find the data cell with player in it 
    positionRow = row.find("td", {"data-stat": "pos"})
    if(positionRow != None):
        position = positionRow.contents[0].text
        # if the player is not a pitcher, process it
        if position != 'P' and position != None:
            print("Position: ")
            print(position)
            create_player_stats(row) 


# printStat()
