from fastapi import APIRouter, status, Depends
from ..database.models import EventsBase, EventsDb
from ..database import events_crud
from ..database.database import get_session
from sqlmodel import Session

router = APIRouter(prefix='/events')