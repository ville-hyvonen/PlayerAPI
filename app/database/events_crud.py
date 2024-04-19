from fastapi import HTTPException
from .models import EventsBase,EventsDb
from sqlmodel import Session, select

