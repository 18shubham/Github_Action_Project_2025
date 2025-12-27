import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home_page(client):
    """Verifies that the home page loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Production-Ready Calculator" in response.data
