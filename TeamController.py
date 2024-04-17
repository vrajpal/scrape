from sqlalchemy import create_engine, text, insert
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

    def create_team(self, new_team):
        print(new_team)
        if new_team != None:
            try:
                with self.engine.connect() as connection:
                    # result = connection.execute(text("select * from team;"))
                    statement = insert(team).values(name=new_team.franchise_name, location=new_team.location)
                    print(statement)
                    compiled = statement.compile()
                    # print(f"""INSERT INTO team (name, location) VALUES ("{team.franchise_name}", "{team.location}");""")
                    # result = connection.execute(text(f"INSERT INTO team (name, location) VALUES '{team.franchise_name}', '{team.location}';"))
                    result = connection.execute(statement)
                    print(result)
            except:
                print("Something failed...")
