# https://fastapi.tiangolo.com/tutorial/sql-databases/
import os

from sqlalchemy import create_engine

# https://stackoverflow.com/questions/15175339/sqlalchemy-what-is-declarative-base/15176114
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL") or os.getenv("SQLALCHEMY_DATABASE_URL")
# if DATABASE_URL.startswith("postgres://"):
#     DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
# https://docs.sqlalchemy.org/en/14/tutorial/engine.html#tutorial-engine

engine = create_engine(
    DATABASE_URL,
)

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
