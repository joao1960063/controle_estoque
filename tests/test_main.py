from fastapi.testclient import TestClient

from controle_estoque.main import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {"message": "Olá Mundo!"}
