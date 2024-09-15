from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


config = dotenv_values(".env")
connection_string = f"""mysql+pymysql://{config['MYSQL_USERNAME']}:{config['MYSQL_PASSWORD']}@{config['MYSQL_HOST']}:{config['MYSQL_PORT']}/{config['DATABASE_NAME']}"""

# Create the database engine
engine = create_engine(connection_string, echo=True)

# Create the base class for declarative models
Base = declarative_base()

# Create a session factory
Session = sessionmaker(bind=engine)