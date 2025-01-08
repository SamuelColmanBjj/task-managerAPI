from fastapi.testclient import TestClient
from app.main import app
import pytest

@pytest.fixture
def client():
    return TestClient(app)

def test_create_task(client):
    response = client.post("/tasks/", json={"name": "Test Task"})
    assert response.status_code == 200
    assert response.json() == {"name": "Test Task", "completed": False}

def test_get_task(client):
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Task", "completed": False}

def test_task_not_found(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404
