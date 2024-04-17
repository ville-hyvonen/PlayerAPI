from fastapi import HTTPException
from .models import EventsDb, EventCreate
from sqlmodel import Session, select
from ..database import player_crud
from datetime import datetime


def get_events(session: Session, type: str = ""):
  if type == "level_started":
    return session.exec(select(EventsDb).where(EventsDb.type == type)).all()
  elif type == "level_solved":
    return session.exec(select(EventsDb).where(EventsDb.type == type)).all()
  return session.exec(select(EventsDb)).all()


def create_event(session: Session, player_id: int, event_in: EventCreate):
  player = player_crud.get_player(session, player_id)
  if not player:
    raise HTTPException(status_code=404, detail=f"Player with id {player_id} not found.")
  event_db = EventsDb.model_validate(event_in)
  event_db.timestamp = datetime.now()
  event_db.player_id = player_id
  session.add(event_db)
  session.commit()
  session.refresh(event_db)
  return event_db