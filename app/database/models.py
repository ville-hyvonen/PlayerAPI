from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from pydantic import BaseModel


class Response(BaseModel):
  id: int
  name: str

class EventResponse(BaseModel):
  id: int
  type: str
  detail: str
  timestamp: datetime
  player_id: int

class PlayerBase(SQLModel):
  name: str = Field(index=True)

class Player(PlayerBase, table=True):
  id: int | None = Field(default=None, primary_key=True)
  events: List["Event"] = Relationship(back_populates="player")

class PlayerCreate(PlayerBase):
  pass

class PlayerPublic(PlayerBase):
  id: int

class EventBase(SQLModel):
  type: str
  detail: str
  player_id: int
  timestamp: datetime

class Event(EventBase, table=True):
  id: int | None = Field(default=None, primary_key=True)
  player_id: int = Field(foreign_key="player.id")
  player: Player = Relationship(back_populates="events")

class EventCreate(EventBase):
  pass

class EventPublic(EventBase):
  id: int