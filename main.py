from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.baseball-reference.com/teams/SEA/2023.shtml')
soup = BeautifulSoup(page.content, 'lxml')
all_team_batting = soup.find("div", {"id": "div_team_batting"})
print(all_team_batting.children)
