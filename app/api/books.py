from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.users import get_current_user
from app.core.crud import crud_books
from app.core.database import get_db
from app.core import schemas

router = APIRouter(tags=["books"], dependencies=[Depends(get_current_user)])


@router.post("/books/")
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # TODO: Validate if a book already exists under that title
    return crud_books.create_book(db=db, book=book)


@router.get("/books/")
async def read_books(db: Session = Depends(get_db)):
    return crud_books.get_all_books(db=db)
