# https://fastapi.tiangolo.com/tutorial/bigger-applications/#the-main-fastapi
from fastapi import FastAPI

from app.api import books

app = FastAPI()

app.include_router(books.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


@app.get("/health/")
async def healthcheck():
    # TODO: test db connection as well https://docs.sqlalchemy.org/en/14/core/engines.html
    return {"status": "ok"}
