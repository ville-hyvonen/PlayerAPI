from fastapi import APIRouter, status, Depends, HTTPException
from ..database.models import Player, PlayerPublic, PlayerCreate, Response
from ..database.database import get_session, engine
from sqlmodel import Session, select
from typing import List

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
  

@router.get("/{id}", response_model=Response)
def get_player(*, session: Session = Depends(get_session), id: int):
  player = session.get(Player, id)
  if not player:
    raise HTTPException(status_code=404, detail="ID not found.")
  return player