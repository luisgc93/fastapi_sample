# https://fastapi.tiangolo.com/tutorial/sql-databases/
import os

from sqlalchemy import create_engine

# https://stackoverflow.com/questions/15175339/sqlalchemy-what-is-declarative-base/15176114
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL").replace("://", "ql://", 1)

# https://docs.sqlalchemy.org/en/14/tutorial/engine.html#tutorial-engine
engine = create_engine(
    "postgresql://qnqdmvyzeatxjz:ed1dbe69e06a9177eec9283aab9832426e9f9fd1a9a31730f5a782f03a90b05f@ec2-34-251-245-108.eu-west-1.compute.amazonaws.com:5432/d1jnt3lodq1srt",
)

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
