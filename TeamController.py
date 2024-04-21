from os import name
from sqlalchemy import create_engine, text, insert
from dotenv import dotenv_values

from db import Session
from models import Team


class TeamController:

    def __init__(self, team) -> None:
        self.team = team
        self.session = Session()
        print("Team Controller")

    # Create Team (Team)
    # Get Team (Team)
    # Delete Team (Team)

    def create_team(self):
        new_team = Team(name=self.team.name, franchise_location=self.team.franchise_location)
