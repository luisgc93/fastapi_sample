from unittest.mock import ANY

from app.core.models import User


class TestUsers:
    def test_returns_200_and_creates_user_when_payload_is_valid(
            self, client, session
    ):

        payload = {
            "username": "user123",
            "password": "safe-pass123",
        }
        response = client.post(
            "/users/",
            json=payload
        )

        assert response.status_code == 200
        assert session.query(User).count() == 1


class TestLogin:
    def test_returns_200_and_access_token_when_valid(self, client, session):
        user_data = {
            "username": "user123",
            "password": "safe-pass123",
        }
        response = client.post(
            "/users/",
            json=user_data
        )

        assert response.status_code == 200
        assert session.query(User).count() == 1

        response = client.post(
            "/login/",
            json=user_data
        )

        assert response.status_code == 200
        assert response.json() == {"access_token": ANY, "token_type": "bearer"}
