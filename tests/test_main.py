from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200


def test_get_expenses():
    response = client.get("/expenses")

    assert response.status_code == 200
    assert "expenses" in response.json()


def test_total_expenses():
    response = client.get("/total-expenses")

    assert response.status_code == 200
    assert response.json()["total_expenses"] == 1350