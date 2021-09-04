# https://fastapi.tiangolo.com/tutorial/sql-databases/
import os

from sqlalchemy import create_engine

# https://stackoverflow.com/questions/15175339/sqlalchemy-what-is-declarative-base/15176114
from sqlalchemy.engine import make_url
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
# should the url contain the driver name? i.e psycopg2


url = make_url(SQLALCHEMY_DATABASE_URL)
print("MAKE URL RESULT: " + url)
# https://docs.sqlalchemy.org/en/14/tutorial/engine.html#tutorial-engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
