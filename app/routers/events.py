from fastapi import APIRouter, status, Depends, Query
from ..database.models import EventPublic, Event, EventResponse
from ..database import events_crud
from ..database.database import get_session
from sqlmodel import Session, select

router = APIRouter(prefix='/events')


@router.get("/", response_model=list[EventResponse])
def get_events(session: Session = Depends(get_session), type: str = Query(None)):
  query = select(Event)
  if type:
    query = query.where(Event.type == type)
  events = session.exec(query).all()
  return events