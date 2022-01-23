from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from app.core import schemas, models


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = generate_password_hash(user.password)
    user = models.User(
        username=user.username,
        hashed_password=hashed_password,
        email=user.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_all_users(db: Session):
    return db.query(models.User).all()
