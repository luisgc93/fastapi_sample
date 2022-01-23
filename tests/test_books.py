from app.core.models import Book, User
from tests.conftest import login


class TestPostBooks:
    def test_returns_200_and_creates_book_when_payload_is_valid(
            self, client, user, session
    ):
        auth = login(client, user)
        payload = {
            "title": "Harry Potter and the Philosopher's Stone",
            "author": "J. K. Rowling"
        }
        response = client.post(
            "/books/",
            json=payload,
            headers=auth
        )

        assert response.status_code == 200
        assert session.query(Book).count() == 1

    def test_returns_422_when_book_title_already_exists(
            self, client, user, session
    ):
        auth = login(client, user)
        payload = {
            "title": "Harry Potter and the Philosopher's Stone",
            "author": "J. K. Rowling"
        }
        response = client.post("/books/", json=payload, headers=auth)

        assert response.status_code == 200

        response = client.post("/books/", json=payload, headers=auth)
        assert response.status_code == 422
        assert response.json()["detail"] == "A book with title Harry Potter and " \
                                            "the Philosopher's Stone already exists."

    def test_returns_422_when_payload_is_invalid(
            self, client, user, session
    ):
        auth = login(client, user)
        payload = {
            "key": "value",
        }
        response = client.post(
            "/books/",
            json=payload,
            headers=auth
        )

        assert response.status_code == 422
        assert session.query(Book).count() == 0

    def test_returns_401_when_user_is_not_authenticated(
            self, client, user
    ):
        payload = {
            "title": "Harry Potter and the Philosopher's Stone",
            "author": "J. K. Rowling"
        }
        response = client.post(
            "/books/",
            json=payload,
        )

        assert response.status_code == 401


class TestGetBooks:
    def test_returns_200_and_books_when_valid(
            self, client, user, book, session
    ):
        auth = login(client, user)

        response = client.get(
            "/books/",
            headers=auth
        )

        assert response.status_code == 200
        assert session.query(Book).count() == 1
        assert response.json()[0] == {
            "title": "J. K. Rowling",
            "author": "Harry Potter and the Philosopher's Stone",
            "pages": 223,
            "id": 1
        }

    def test_returns_401_when_user_is_not_authenticated(
            self, client, user
    ):

        response = client.get(
            "/books/",
        )

        assert response.status_code == 401
