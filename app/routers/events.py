from fastapi import APIRouter, status, Depends, HTTPException
from ..database.models import EventsBase, EventsDb, EventCreate
from ..database import events_crud
from ..database.database import get_session
from sqlmodel import Session
from typing import Optional

router = APIRouter(prefix="/events")


#Hae kaikki eventit
@router.get("/", response_model=list[EventsDb])
def get_events(session: Session = Depends(get_session), type: Optional[str] = None):
  if type:
    if type not in ["level_started", "level_solved"]:
      raise HTTPException(status_code=400, detail="Wrong type.")
    events = events_crud.get_events(session, type)
  else:
    events = events_crud.get_events(session)
  return events


@router.post("/players/{id}/events", status_code=status.HTTP_201_CREATED)
def create_event(*, session: Session = Depends(get_session), id: int, event_in: EventCreate):
  event = events_crud.create_event(session, id, event_in)
  return event