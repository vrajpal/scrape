from sqlalchemy import String 
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from db import Base

class Player(Base):
    __tablename__ = "player"

    player_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    age: Mapped[int] = mapped_column(Integer)
    team_id: Mapped[int] = mapped_column(Integer, ForeignKey("team.id"))
    position: Mapped[str] = mapped_column(String(255))

    def __init__(self, player) -> None:
        self.player = player



