from sqlalchemy.orm import Session

from app.core.schemas import schemas
from app.core.models import models


def get_book(db: Session, book_id: int):

    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_book_by_title(db: Session, title: str):

    return db.query(models.Book).filter(models.Book.title == title).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
