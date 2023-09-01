from sqlalchemy import create_engine
from sqlalchemy import text
from dotenv import dotenv_values

# read mysql config (dev is local mysql on pc)
config = dotenv_values(".env") 
# print out config to verify
# print(config)
# create connection to mysql using pymysql driver (dev is local pc)
engine = create_engine(f"mysql+pymysql://{config['MYSQL_USER']}:{config['MYSQL_PASSWORD']}@{config['MYSQL_HOST']}:{config['MYSQL_PORT']}/scrape_mlb")

# test function to verify connection to db
def printStat():
    with engine.connect() as connection:
        result = connection.execute(text("select * from stat"))
        for row in result:
            print(row)

INSERT_STAT_OPEN = "INSERT INTO stat (value, player_id, team_id, stat_name, stat_abbrev) "
VALUES = "VALUES("
CLOSE_VALUES = ")"
INSERT_TEAM_OPEN = "INSERT INTO team (name, location)"
CLOSE_INSERT = ");"

# from a row from baseball ref, insert one stat
def insert_stat(values):
    if values:
        sql_builder = [INSERT_STAT_OPEN]
        sql_builder.append(VALUES)
        sql_builder.append(values)
        sql_builder.append(CLOSE_VALUES)
        sql_builder.append(CLOSE_INSERT)
    print(sql_builder)
    return sql_builder



def insert_team(engine, teams):
   with engine.connect() as connection:
       connection.execute(text(INSERT_TEAM_OPEN))

def insert_player():
    