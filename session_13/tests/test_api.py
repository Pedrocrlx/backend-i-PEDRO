import pytest
from fastapi.testclient import TestClient
from session_13.main import api
from starlette import status


@pytest.fixture(scope="session")
def client():
    return TestClient(app=api)


def test_api_create_task(client):
    response = client.post("/task")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is not None
