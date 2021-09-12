import os
from datetime import datetime, timedelta

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.crud import crud_users
from app.core.exceptions import CREDENTIALS_EXCEPTION, AUTHENTICATION_EXCEPTION
from app.core.models.database import get_db
from app.core.models.models import User
from app.core.schemas import schemas
from app.core.schemas.schemas import TokenData

from passlib.context import CryptContext
from jose import JWTError, jwt


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)) -> User:
    user = crud_users.get_user_by_username(db, username)
    if not user:
        raise AUTHENTICATION_EXCEPTION
    if not verify_password(password, user.hashed_password):
        raise CREDENTIALS_EXCEPTION
    return user


def create_access_token(data: dict, expires_delta: int):
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, os.getenv("SESSION_AUTH_KEY"), algorithm=os.getenv("ALGORITHM"))

    return encoded_jwt


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, os.getenv("SESSION_AUTH_KEY"), algorithms=[os.getenv("ALGORITHM")])
        username: str = payload.get("sub")
        if username is None:
            raise CREDENTIALS_EXCEPTION
        token_data = TokenData(username=username)
    except JWTError:
        raise CREDENTIALS_EXCEPTION
    user = crud_users.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise CREDENTIALS_EXCEPTION
    return user


@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/login", response_model=schemas.Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password, db)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/users/")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud_users.create_user(db, user)


@router.get("/users/", tags=["users"])
async def read_users(db: Session = Depends(get_db)):
    return crud_users.get_all_users(db=db)
