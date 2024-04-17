from typing import List
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declarative_base

from dotenv import dotenv_values



config = dotenv_values(".env") 
engine = create_engine(f"mysql+pymysql://{config['MYSQL_USER']}:{config['MYSQL_PASSWORD']}@{config['MYSQL_HOST']}:{config['MYSQL_PORT']}/scrape_mlb")

Base = declarative_base()

class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(primary_key=True)
    location: Mapped[str] = mapped_column(String(255)) 
    franchise_name: Mapped[str] = mapped_column((String(255)))

    def __init__(self, franchise_name, location) -> None:
        self.franchise_name = franchise_name
        self.location = location

    def __repr__(self) -> str:
        return f"Team(location={self.location}, franchise_name={self.franchise_name})"
        
