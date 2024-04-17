from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routers import player, events
from .database.database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting...")
    create_db()
    yield
    print("Ending...")

app = FastAPI(lifespan=lifespan)


app.include_router(player.router)
app.include_router(events.router)