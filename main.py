from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.baseball-reference.com/teams/SEA/2023.shtml')
soup = BeautifulSoup(page.content, 'lxml')
all_team_batting = soup.find("table", {"id": "team_batting"}).find_all('tr')
# rows = all_team_batting.find_all('tr');
batting = {}
for row in all_team_batting:
    name_tag = row.find("td", {"data-stat": "player"})
    if name_tag:
        name = row.find("td", {"data-stat": "player"}).contents
        age = row.find("td", {"data-stat": "age"}).contents
        games = row.find("td", {"data-stat": "G"}).contents

        print(name)
        print(age)
        print(games)
    

        # if name[0]:
        #     print(name[0].contents)
        #     print('________________________________________')
            # td data-stat=player
