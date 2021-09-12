from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.crud import crud_books
from app.core.models.database import get_db
from app.core.schemas import schemas

router = APIRouter()


@router.post("/books/", tags=["books"])
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # TODO: Validate if a book already exists under that title
    return crud_books.create_book(db=db, book=book)


@router.get("/books/", tags=["books"])
async def read_books(db: Session = Depends(get_db)):
    return crud_books.get_all_books(db=db)
