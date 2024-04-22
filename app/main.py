from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routers import player, events
from .database.database import create_db
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting...")
    create_db()
    yield
    print("Ending...")

app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(player.router)
app.include_router(events.router)