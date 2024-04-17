from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session
from ..database.models import PlayerDb, EventsDb, PlayersList, PlayerCreate, EventCreate
from ..database import player_crud, events_crud
from ..database.database import get_session
from typing import Optional


router = APIRouter(prefix="/players")


#Tee pelaaja
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_player(*, session: Session = Depends(get_session), player_in: PlayerCreate):
  player = player_crud.create_player(session, player_in)
  return player


#Hae kaikki pelaajat (nimi + id)
@router.get("/", response_model=list[PlayersList])
def get_players(*, session: Session = Depends(get_session)):
  players = player_crud.get_players(session)
  return players

#Hae yhden pelaajan kaikki tiedot
@router.get("/{id}", response_model=PlayerDb)
def get_player(*, session: Session = Depends(get_session), id: int):
  player = player_crud.get_player(session, id)
  if not player:
    raise HTTPException(status_code=404, detail=f"Player with id {id} not found.")
  return player

#Hae yhden pelaajan kaikki eventit + suodatus
@router.get("/{id}/events", response_model=list[EventsDb])
def get_player_events(*, session: Session = Depends(get_session), id: int, type: Optional[str] = None):
  player_events = events_crud.get_events(session, id, type)
  if not player_events:
    raise HTTPException(status_code=404, detail=f"No events for player id {id}")
  return player_events

#Luo event pelaajalle
@router.post("/{id}/events", status_code=status.HTTP_201_CREATED)
def create_event(*, session: Session = Depends(get_session), id: int, event_in: EventCreate):
  player = player_crud.get_player(session, id)
  if not player:
    raise HTTPException(status_code=404, detail=f"Player id {id} not found.")
  if event_in.type not in ["level_started", "level_solved"]:
    raise HTTPException(status_code=400, detail="Wrong event type.")
  event = events_crud.create_event(session, id, event_in)
  return event
