from typing import Optional

from pydantic import BaseModel  # noqa


class Token(BaseModel):
    access_token: str
    token_type: str


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None


class UserCreate(UserBase):
    password: str


class TokenData(BaseModel):
    username: Optional[str] = None


class BookBase(BaseModel):
    title: str
    author: str
    pages: Optional[int]


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        # https://pydantic-docs.helpmanual.io/usage/model_config/
        # https://fastapi.tiangolo.com/tutorial/sql-databases/#use-pydantics-orm_mode
        orm_mode = True
