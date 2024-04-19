from fastapi import APIRouter, status, Depends
from ..database.models import PlayerBase, PlayerDb
from ..database import player_crud
from ..database.database import get_session
from sqlmodel import Session

router = APIRouter(prefix='/players')


#Tee pelaaja
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_player(*, session: Session = Depends(get_session), player_in: PlayerBase):
  return player_crud.create_player(session, player_in)