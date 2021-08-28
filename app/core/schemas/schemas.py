from typing import Optional

from pydantic import BaseModel


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
