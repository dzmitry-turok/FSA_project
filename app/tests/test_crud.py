from app.main import app
from fastapi.testclient import TestClient


def test_create(temp_db):
    request_data = {
        "email": "test@test.com",
    }
    with TestClient(app) as client:
        response = client.post("/create", json=request_data)
    assert response.status_code == 200


def test_get(temp_db):

    with TestClient(app) as client:
        response = client.get("/all_users")
    assert response.status_code == 200


def test_update(temp_db):

    request_data = {
        'id': '1',
        "email": "test2@test2.com",
    }
    with TestClient(app) as client:
        response = client.post("/update", data=request_data)
    assert response.status_code == 200


def test_delete(temp_db):
    request_data = {
        'id': '1',
    }
    with TestClient(app) as client:
        response = client.post("/delete", data=request_data)
    assert response.status_code == 200
