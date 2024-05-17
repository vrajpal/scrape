from os import name
from sqlalchemy import create_engine, text, insert
from dotenv import dotenv_values

from models import Team


class TeamController:

    def __init__(self, session) -> None:
        self.session = session
        print("Team Controller")
    
    def db_insert(self, team):
        with self.session as session:
            if team != None:
                session.add(team)
                session.commit()

    def create_team(self, team):
        self.db_insert(team) 
        print(team.__tablename__)
