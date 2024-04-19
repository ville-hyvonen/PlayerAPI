from fastapi import HTTPException
from .models import PlayerBase, PlayerDb
from sqlmodel import Session, select



#Tee pelaaja
def create_player(session: Session, player_in: PlayerBase):
  playerdb = PlayerDb.model_validate(player_in)
  session.add(playerdb)
  session.commit()
  session.refresh(playerdb)
  response = {"id": playerdb.id, "name": playerdb.name}
  return response

#Hae kaikki pelaajat (nimi + id)
def get_players(session: Session):
  players = session.exec(select(PlayerDb)).all()
  return players