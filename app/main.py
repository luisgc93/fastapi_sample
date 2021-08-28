# https://fastapi.tiangolo.com/tutorial/bigger-applications/#the-main-fastapi
import uvicorn
from fastapi import FastAPI

from .api import books


app = FastAPI()

app.include_router(books.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
