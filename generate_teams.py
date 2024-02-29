# generate teams
# A script that populates the team table in scrape_mlb

import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values

config = dotenv_values(".env") 


page = requests.get("https://www.baseball-reference.com/teams/")

soup = BeautifulSoup(page.content, "lxml")

all_active_teams = soup.find("table", {"id": "teams_active"})

print(all_active_teams)
