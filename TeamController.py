from cgitb import text
from sqlalchemy import create_engine, text
from dotenv import dotenv_values


class TeamController:

    def __init__(self) -> None:
        self.config = dotenv_values(".env")
        connection_string = f"""mysql+pymysql://{self.config['MYSQL_USERNAME']}:{self.config['MYSQL_PASSWORD']}@{self.config['MYSQL_HOST']}:{self.config['MYSQL_PORT']}/{self.config['DATABASE_NAME']}"""
        print(connection_string)
        self.engine = create_engine(connection_string)

    def print_config(self):
        print(self.config)

    # Create Team (Team)
    # Get Team (Team)
    # Delete Team (Team)

    def create_team(self, team):
        team.print_team()
        if team != None:
            try:
                with self.engine.connect() as connection:
                    # result = connection.execute(text("select * from team;"))
                    print(f"""INSERT INTO team (name, location) VALUES ("{team.franchise_name}", "{team.location}");""")
                    result = connection.execute(text(f"""INSERT INTO team (name, location) VALUES ('{team.franchise_name}', '{team.location}');"""))
                    print(result)
            except:
                print("Something failed...")
