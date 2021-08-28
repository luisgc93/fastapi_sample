# https://fastapi.tiangolo.com/tutorial/bigger-applications/#the-main-fastapi

from fastapi import FastAPI

from .api import books


app = FastAPI()

app.include_router(books.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
