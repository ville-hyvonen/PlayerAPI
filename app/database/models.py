from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class EventsBase(SQLModel):
  type: str
  detail: str
  timestamp: datetime
  player_id: int


class PlayerBase(SQLModel):
  name: str


#En saanut listiä toimimaan, oli pakko säätää viiteavaimet ja relaatio
class PlayerDb(PlayerBase, table=True):
  __tablename__ = "players"
  id: int = Field(default=None, primary_key=True)
  name: str
  events: List['EventsDb'] = Relationship(back_populates="player")


#En saanut listiä toimimaan, oli pakko säätää viiteavaimet ja relaatio
class EventsDb(EventsBase, table=True):
  id: int = Field(default=None, primary_key=True)
  type: str
  detail: str
  timestamp: datetime = Field(default=datetime.now)
  player_id: int = Field(foreign_key="players.id")
  player: Optional['PlayerDb'] = Relationship(back_populates="events")


class PlayerCreate(PlayerBase):
  pass


class EventCreate(SQLModel):
  type: str
  detail: str
  timestamp: Optional[datetime] = None
  player_id: Optional[int] = None


class PlayersList(SQLModel):
  id: int
  name: str


class PlayerEvents(SQLModel):
  id: int
  name: str
  events: Optional[list] = None