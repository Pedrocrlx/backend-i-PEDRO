import pytest

# Create your tests here.


@pytest.mark.django_db
def test_homepage(client):
    response = client.get("/")
    assert response
    assert response.status_code == 200
