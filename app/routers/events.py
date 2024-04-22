from fastapi import APIRouter, Depends, Query, status, HTTPException
from ..database.models import Event, EventResponse
from ..database.database import get_session
from sqlmodel import Session, select

router = APIRouter(prefix='/events')


@router.get("/", response_model=list[EventResponse])
def get_events(session: Session = Depends(get_session), type: str = Query(None)):
  if type is not None:
    check_type = {"level_started", "level_solved"}
    if type not in check_type:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong type.")
  query = select(Event)
  if type:
    query = query.where(Event.type == type)
  events = session.exec(query).all()
  return events