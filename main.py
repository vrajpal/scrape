from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.baseball-reference.com/teams/SEA/2023.shtml')
soup = BeautifulSoup(page.content, 'lxml')
print(soup.find("div", {"id": "all_team_batting"}))
