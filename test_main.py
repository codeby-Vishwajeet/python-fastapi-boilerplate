from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "environment": "production"}

def test_get_items():
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert len(response.json()) == 2
