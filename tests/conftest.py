import pytest
from fastapi.testclient import TestClient
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import scoped_session, sessionmaker

from app.core import models
from app.core.database import engine, Base, SessionLocal
from app.main import app


def _reset_schema():
    db = SessionLocal()
    for table in Base.metadata.sorted_tables:
        db.execute(
            'TRUNCATE {name} RESTART IDENTITY CASCADE;'.format(name=table.name)
        )
        db.commit()


@pytest.fixture
def test_db():
    yield engine
    engine.dispose()
    _reset_schema()


@pytest.fixture
def session(test_db):
    connection = test_db.connect()
    trans = connection.begin()
    db = scoped_session(sessionmaker(bind=engine))
    try:
        yield db
    finally:
        db.close()
    trans.rollback()
    connection.close()
    db.remove()


@pytest.fixture
def client(session):
    yield TestClient(app)


class BookFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Book
        sqlalchemy_session = session
