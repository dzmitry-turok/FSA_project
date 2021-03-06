from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_check_work():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Check_work": "True"}
