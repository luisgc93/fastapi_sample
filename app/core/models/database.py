# https://fastapi.tiangolo.com/tutorial/sql-databases/
import os

from sqlalchemy import create_engine

# https://stackoverflow.com/questions/15175339/sqlalchemy-what-is-declarative-base/15176114
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# DATABASE_URL = os.getenv("DATABASE_URL").replace("://", "ql://", 1)

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
DATABASE_URL = f"postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:5432/${POSTGRES_DB}"

print(f"Database URL: {DATABASE_URL}")
# https://docs.sqlalchemy.org/en/14/tutorial/engine.html#tutorial-engine
engine = create_engine(
    DATABASE_URL,
)

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
