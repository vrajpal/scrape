from bs4 import BeautifulSoup, Tag


def all_team_batting(soup):
    all_team_batting = soup.find("table", {"id": "team_batting"})
    if all_team_batting:
        tbody = all_team_batting.find("tbody")
    if isinstance(tbody, Tag):
        return tbody.find_all('tr')
    else:
        return []
