from os import name
from sqlalchemy import create_engine, text, insert
from dotenv import dotenv_values

from db import Session
from models import Team


class TeamController:

    def __init__(self) -> None:
        self.session = Session()
        print("Team Controller")

    # Create Team (Team)
    # Get Team (Team)
    # Delete Team (Team)

    def create_team(self, team):
        new_team = Team.Team(team.franchise_name, team.location)
        print(new_team.__str__())
