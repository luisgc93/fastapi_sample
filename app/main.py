# https://fastapi.tiangolo.com/tutorial/bigger-applications/#the-main-fastapi

from fastapi import FastAPI

from app.api import books
from app.core.models.database import engine

app = FastAPI()

app.include_router(books.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


@app.get("/health/")
async def healthcheck():
    with engine.connect():
        return {"status": "ok"}
