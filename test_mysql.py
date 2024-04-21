from dotenv import dotenv_values
from sqlalchemy import create_engine, text 


config = dotenv_values(".env")
connection_string = f"""mysql://{config['MYSQL_USERNAME']}:{config['MYSQL_PASSWORD']}@{config['MYSQL_HOST']}:{config['MYSQL_PORT']}/{config['DATABASE_NAME']}"""
print(connection_string)
engine = create_engine(connection_string)
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM team LIMIT 1"))
    print(result.all())
