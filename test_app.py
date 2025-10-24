from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_status(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_page_content(client):
    response = client.get('/')
    assert b"Hola, Mundo!" in response.data

def test_home_page_param(client):
    response = client.get('/?nombre=Equipo')
    assert b"Hola, Equipo!" in response.data
