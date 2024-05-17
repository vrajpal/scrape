from sqlalchemy import String 
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declarative_base

from db import Base

class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(primary_key=True)
    location: Mapped[str] = mapped_column(String(255)) 
    name: Mapped[str] = mapped_column((String(255)))

    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location

    def __repr__(self) -> str:
        return f"Team(location={self.location}, name={self.name})"
        
