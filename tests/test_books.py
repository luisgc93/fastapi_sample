
class TestBooks:
    def test_returns_200_and_creates_book_when_payload_is_valid(
            self, client
    ):

        payload = {
            "title": "Harry Potter and the Philosopher's Stone",
            "author": "J. K. Rowling"
        }
        response = client.post(
            "/books/",
            json=payload
        )

        assert response.status_code == 200

    def test_returns_422_when_payload_is_invalid(self):
        pass
