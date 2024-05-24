import sys, os

from main.ai_agents_library.repositories.core.agents_repository import AgentsRepository
from main.library.di_container import Container
sys.path.insert(0, os.path.abspath("."))

container: Container = Container()
agents_repository: AgentsRepository = container.agents_repository()

def test_should_get_agents(mocker):
    # Mocks
    successResponse = mocker.Mock()
    successResponse.status = 200
    successResponse.read.return_value = b'{"object":"list","results":[],"has_more":false,"next_cursor":null}'
    conn = mocker.Mock()
    conn.getresponse.return_value = successResponse
    mocker.patch("http.client.HTTPSConnection", return_value=conn)

    # Arrange
    page_size = 100
    initial_cursor = None
    body = None

    # Act
    response_data: dict = agents_repository.get_agents(page_size, initial_cursor, body)

    # Assert
    assert response_data is not None
    assert "results" in response_data
    assert "object" in response_data
    assert response_data["object"] == "list"
    assert "has_more" in response_data
    assert "next_cursor" in response_data
    assert "results" in response_data
    assert "results" in response_data
    assert "object" in response_data
    assert response_data["object"] == "list"
    assert "has_more" in response_data
    assert "next_cursor" in response_data
