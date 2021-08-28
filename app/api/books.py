from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.crud import crud_books
from app.core.models.database import SessionLocal
from app.core.schemas import schemas

router = APIRouter()


def get_db():
    # Dependency https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-dependency
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/books/", tags=["books"])
async def read_books():
    return {"title": "Harry Potter"}


@router.post("/books/", tags=["books"])
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud_books.create_book(db=db, book=book)
