from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.schemas import schemas
from app.core.models import models


def _get_password_hash(password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = _get_password_hash(user.password)
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
