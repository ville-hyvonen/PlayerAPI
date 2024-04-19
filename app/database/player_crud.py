from fastapi import HTTPException
from .models import PlayerBase, PlayerDb, PlayerCreate
from sqlmodel import Session, select



#Tee pelaaja
def create_player(session: Session, player_in: PlayerBase):
  playerdb = PlayerDb.model_validate(player_in)
  session.add(playerdb)
  session.commit()
  session.refresh(playerdb)
  response = {"id": playerdb.id, "name": playerdb.name}
  return response