from dotenv import dotenv
from sqlalchemy import create_engine, text
from db import Session

session = Session()

config = dotenv_values(".env")


session

