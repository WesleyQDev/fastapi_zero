from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Este teste tem 3 etapas (AAA
    A: Arrange - Arrajo
    A: Act     - Executa a coisa (o SUT)
    A: Assert  - Garamta que A é A
    """
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_landing_page_deve_retornar_html():
    """
    Testa se a landing page retorna o HTML esperado
    """
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/landing-page')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert '<h1>Welcome to the Landing Page</h1>' in response.text
