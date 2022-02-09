import os
from datetime import datetime, timedelta

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash

from app.core.crud import crud_users
from app.core.exceptions import CREDENTIALS_EXCEPTION, AUTHENTICATION_EXCEPTION
from app.core.database import get_db
from app.core.models import User
from app.core import schemas
from app.core.schemas import TokenData, UserCreate, UserRead

from jose import JWTError, jwt


router = APIRouter(tags=["users"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_password(plain_password, hashed_password):
    return check_password_hash(hashed_password, plain_password)


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)) -> User:
    user = crud_users.get_user_by_username(db, username)
    if not user:
        raise AUTHENTICATION_EXCEPTION
    if check_password_hash(user.hashed_password, password) is False:
        raise CREDENTIALS_EXCEPTION
    return user


def create_access_token(data: dict, expires_delta: int):
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, os.getenv("SESSION_AUTH_KEY"), algorithm=os.getenv("ALGORITHM"))

    return encoded_jwt


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
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


@router.post("/login/", response_model=schemas.Token)
async def login_for_access_token(credentials: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(credentials.username, credentials.password, db)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/users/")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud_users.get_user_by_username(db, username=user.username):
        raise HTTPException(status_code=422, detail=f"A user with username {user.username} already exists.")
    user = crud_users.create_user(db, user)
    return UserRead.from_orm(user)


@router.get("/users/")
async def read_users(db: Session = Depends(get_db)):
    return crud_users.get_all_users(db=db)
