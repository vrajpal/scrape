from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.baseball-reference.com/teams/SEA/2023.shtml')
soup = BeautifulSoup(page.content, 'lxml')
all_team_batting = soup.find("table", {"id": "team_batting"}).find_all('tr')
# rows = all_team_batting.find_all('tr');
# the headers for the batting table in Baseball Ref, remove player as its method for grabbing name is inconsistent 
batting = {"age", "G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SB", 
    "CS", "BB", "SO", "batting_avg", "onbase_perc", "slugging_perc", "onbase_plus_slugging", 
    "onbase_plus_slugging_plus", "TB", "GIDP", "HBP", "SH", "SF", "IBB"}

def create_player_stats(row):
    player_row = {}
    name = row.find("td", {"data-stat": "player"}).contents[0].text
    for stat in batting:
        value = row.find("td", {"data-stat": stat}).contents
        player_row[stat] = value
    print(name)
    print(player_row)

# for each player in the batting table, parse it
for row in all_team_batting:
    # find the data cell with player in it 
    name_tag = row.find("td", {"data-stat": "player"})
    if name_tag:
        # grab the name, games played and age. 
       create_player_stats(row) 
