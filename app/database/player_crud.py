from fastapi import HTTPException
from .models import PlayerDb, PlayerCreate, PlayersList
from sqlmodel import Session, select

#Luo pelaaja
def create_player(session: Session, player_in: PlayerCreate):
  player_db = PlayerDb.model_validate(player_in)
  session.add(player_db)
  session.commit()
  session.refresh(player_db)
  return player_db

#Hae pelaajat (nimi + id)
def get_players(session: Session):
  players = session.exec(select(PlayerDb)).all()
  return [PlayersList(id = player.id, name = player.name) for player in players]
    
#Hae yhden pelaajan kaikki tiedot
def get_player(session: Session, id: int):
  player = session.get(PlayerDb, id)
  if not player:
    raise HTTPException(status_code=404, detail=f"Player with id {id} not found.")
  return player


