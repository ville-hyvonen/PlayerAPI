from fastapi import APIRouter, status, Depends, HTTPException, Path, Query
from ..database.models import Player, PlayerCreate, Response, Event, EventCreate, EventResponse, PlayerWithEventsResponse
from ..database.database import get_session
from sqlmodel import Session, select
from typing import List
from datetime import datetime

router = APIRouter(prefix='/players')


#Tee pelaaja
@router.post("/", response_model=Response, status_code=status.HTTP_201_CREATED)
def create_player(*, session: Session = Depends(get_session), player: PlayerCreate):
  playerdb = Player.model_validate(player)
  session.add(playerdb)
  session.commit()
  session.refresh(playerdb)
  response = {"id": playerdb.id, "name": playerdb.name}
  return response


@router.get("/", response_model=list[Response])
def get_players(*, session: Session = Depends(get_session)):
  players = session.exec(select(Player)).all()
  return players
  

@router.get("/{id}", response_model=PlayerWithEventsResponse)
def get_player(*, session: Session = Depends(get_session), id: int):
  player = session.get(Player, id)
  if not player:
    raise HTTPException(status_code=404, detail="ID not found.")
  return player

@router.post("/{id}/events", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(data: EventCreate, id: int = Path(...), session: Session = Depends(get_session)):
  player = session.get(Player, id)
  if not player:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found.")
  check_type = ["level_started", "level_solved"]
  if data.type not in check_type:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong type.")
  new_event = Event(type=data.type, detail=data.detail, player_id=id, timestamp=datetime.now())
  session.add(new_event)
  session.commit()
  return new_event

@router.get("/{id}/events", response_model=List[EventResponse])
def get_player_events(id: int, type: str = Query(None), session: Session = Depends(get_session)):
  player = session.get(Player, id)
  if player is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found.")
  query = select(Event).filter(Event.player_id == id)
  if type is not None:
    check_types = {"level_started", "level_solved"}
    if type not in check_types:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong type.")
  if type:
    query = query.filter(Event.type == type)
  events = session.exec(query).all()
  return events