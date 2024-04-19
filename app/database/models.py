from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import List, Optional


class PlayerBase(SQLModel):
  name: str


class PlayerDb(PlayerBase, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str


class PlayerCreate(PlayerBase):
  pass


class EventsBase(SQLModel):
  type: str
  detail: str
  player_id: int
  timestamp: datetime


class EventsDb(EventsBase, table=True):
  id: int = Field(default=None, primary_key=True)


class PlayerWithEvents(PlayerBase):
  events: List[EventsBase] = []