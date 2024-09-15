from sqlalchemy import String 
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from utils import convertPositionToEnum

from db import Base

class Player(Base):
    __tablename__ = "player"

    player_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    age: Mapped[int] = mapped_column(Integer)
    team_id: Mapped[int] = mapped_column(Integer)
    position: Mapped[int] = mapped_column(Integer)

    def __init__(self, first_name, last_name, age, team_id, position) -> None:
        positionNum = convertPositionToEnum(position)
         
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.team_id = team_id
        if positionNum:
            self.position = positionNum
        else:
            self.position = 0
    
    def __repr__(self) -> str:
        return f"Player(first_name={self.first_name}, last_name={self.last_name}, age={self.age}, team_id={self.team_id}, position={self.position})"



