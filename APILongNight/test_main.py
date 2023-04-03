from main import app
from starlette.testclient import TestClient

client = TestClient(app)

def test_get_clientes():

    response = client.get('/clientes')
    assert response.status_code == 200

