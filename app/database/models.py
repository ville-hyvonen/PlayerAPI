from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import List, Optional


class PlayerBase(SQLModel):
  id: int
  name: str
  events: Optional[str]

class PlayerDb(PlayerBase, table=True):
  id: int = Field(default=None, primary_key=True)

class PlayerCreate(PlayerBase):
  pass

class EventsBase(SQLModel):
  id: int
  type: str
  detail: str
  player_id: int
  timestamp: datetime

class EventsDb(EventsBase, table=True):
  id: int = Field(default=None, primary_key=True)