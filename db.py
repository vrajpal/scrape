"""
Database configuration module.
"""

from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


required_keys = ['MYSQL_USERNAME', 'MYSQL_PASSWORD', 'MYSQL_HOST', 'MYSQL_PORT', 'DATABASE_NAME']
missing_keys = [key for key in required_keys if key not in (dotenv_values(".env"))]

if missing_keys:
    raise KeyError(f"Missing required environment variables: {', '.join(missing_keys)}")

connection_string = (
    f"mysql+pymysql://{(dotenv_values(".env"))['MYSQL_USERNAME']}:"
    f"{(dotenv_values(".env"))['MYSQL_PASSWORD']}@"
    f"{(dotenv_values(".env"))['MYSQL_HOST']}:"
    f"{(dotenv_values(".env"))['MYSQL_PORT']}/"
    f"{(dotenv_values(".env"))['DATABASE_NAME']}"
)

# Create the database engine
engine = create_engine(connection_string, echo=True)

# Create the base class for declarative models
Base = declarative_base()

# Create a session factory
Session = sessionmaker(bind=engine)
