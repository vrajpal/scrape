# generate teams
# A script that populates the team table in scrape_mlb

import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values

config = dotenv_values(".env") 


page = requests.get("https://www.baseball-reference.com/teams/")

soup = BeautifulSoup(page.content, "lxml")

all_active_teams = soup.find("table", {"id": "teams_active"})
table_body = all_active_teams.find("tbody")
team_headers = table_body.find_all("th", class_="right")
rows = [th.find_parent("tr") for th in team_headers]
if rows != None:
    for row in rows:
        # print("========================")
        # print(row.prettify())
        # print("========================")
        cols = row.find_all('td')
        for col in cols:
            print(col['data-stat'])
            print(col.text)


# if all_active_teams != None:
#    prettyTeams = all_active_teams.prettify()
# else:
#    prettyTeams = all_active_teams

#print(prettyTeams)
