from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_add_route():
    response = client.get("/add", params={"a": 3, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 7.0}
