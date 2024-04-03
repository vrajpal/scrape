from dotenv import dotenv_values
from sqlalchemy import create_engine


config = dotenv_values(".env")
connection_string = (f"""mysql://{config['MYSQL_USERNAME']}:{config['MYSQL_PASSWORD']}@{config['MYSQL_HOST']}:{config['MYSQL_PORT']}/{config['DATABASE_NAME']}""")
print(connection_string)
engine = create_engine(connection_string)
engine.connect()
 