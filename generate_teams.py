# generate teams
# A script that populates the team table in scrape_mlb

import requests
from TeamController import TeamController
from bs4 import BeautifulSoup
from dotenv import dotenv_values
from models.Team import Team

config = dotenv_values(".env") 


page = requests.get("https://www.baseball-reference.com/teams/")

soup = BeautifulSoup(page.content, "lxml")
team_controller = TeamController()
all_active_teams = soup.find("table", {"id": "teams_active"})
table_body = all_active_teams.find("tbody")
team_headers = table_body.find_all("th", class_="right")
rows = [th.find_parent("tr") for th in team_headers]
if rows != None:
    for row in rows:
        cols = row.find_all('td')
        for col in cols:
            col_name = col['data-stat']
            col_value = col.text
            if col_name == 'franchise_name':
                franchise_vals = col_value.split()
                if franchise_vals != None:
                    if len(franchise_vals) == 3:
                        franchise_location = franchise_vals[0] + " " + franchise_vals[1]
                        franchise_name = franchise_vals[2]
                    else: 
                        franchise_location = franchise_vals[0]
                        franchise_name = franchise_vals[1]
                    team = Team(franchise_name, franchise_location)
                    team_controller.create_team(team)
