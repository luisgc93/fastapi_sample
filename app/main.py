# https://fastapi.tiangolo.com/tutorial/bigger-applications/#the-main-fastapi

from fastapi import FastAPI

from app.api import books, users
from app.core.models.database import engine

app = FastAPI()

app.include_router(books.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Library API!"}


@app.get("/health/")
async def healthcheck():
    with engine.connect():
        return {"status": "ok"}
