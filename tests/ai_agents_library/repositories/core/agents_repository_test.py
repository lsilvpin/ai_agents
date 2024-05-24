import sys, os

from main.ai_agents_library.repositories.core.agents_repository import AgentsRepository
from main.library.di_container import Container

sys.path.insert(0, os.path.abspath("."))

container: Container = Container()
agents_repository: AgentsRepository = container.agents_repository()


def test_should_create_agent(mocker):
    # Mocks
    successResponse = mocker.Mock()
    successResponse.status = 200
    sample: str = (
        '{"object":"page","id":"48a4c8b5-8c75-43ee-8863-505c38ffa20e","created_time":"2024-05-24T01:47:00.000Z","last_edited_time":"2024-05-24T01:47:00.000Z","created_by":{"object":"user","id":"27910b45-ae07-403c-b7e9-35b5adc896af"},"last_edited_by":{"object":"user","id":"27910b45-ae07-403c-b7e9-35b5adc896af"},"cover":null,"icon":{"type":"emoji","emoji":"👩🏻‍💻"},"parent":{"type":"database_id","database_id":"6301f640-e21c-4526-a72e-d96e7d4ba71d"},"archived":false,"in_trash":false,"properties":{"Papel":{"id":"PqtR","type":"rich_text","rich_text":[{"type":"text","text":{"content":"Exemplo de Papel","link":null},"annotations":{"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Exemplo de Papel","href":null}]},"Objetivo":{"id":"TF%7BM","type":"rich_text","rich_text":[{"type":"text","text":{"content":"Exemplo de objetivo","link":null},"annotations":{"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Exemplo de objetivo","href":null}]},"Nome":{"id":"title","type":"title","title":[{"type":"text","text":{"content":"Exemplo de nome","link":null},"annotations":{"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Exemplo de nome","href":null}]}},"url":"https://www.notion.so/Exemplo-de-nome-48a4c8b58c7543ee8863505c38ffa20e","public_url":null,"developer_survey":"https://notionup.typeform.com/to/bllBsoI4?utm_source=postman","request_id":"ec85c21d-2495-4a2c-a5ca-8e4e1ab1bc26"}'
    )
    successResponse.read.return_value = sample.encode("utf-8")
    conn = mocker.Mock()
    conn.getresponse.return_value = successResponse
    mocker.patch("http.client.HTTPSConnection", return_value=conn)

    # Arrange
    nome = "Exemplo de nome"
    papel = "Exemplo de Papel"
    objetivo = "Exemplo de objetivo"
    image_url = "https://host:port/path/to/image.jpg"

    # Act
    response_data: dict = agents_repository.create_agent(
        nome, papel, objetivo, image_url
    )

    # Assert
    assert response_data is not None
    assert "object" in response_data
    assert response_data["object"] == "page"
    assert "Nome" in response_data["properties"]
    assert "Objetivo" in response_data["properties"]
    assert "Papel" in response_data["properties"]
    assert response_data["properties"]["Nome"]["title"][0]["text"]["content"] == nome
    assert (
        response_data["properties"]["Objetivo"]["rich_text"][0]["text"]["content"]
        == objetivo
    )
    assert (
        response_data["properties"]["Papel"]["rich_text"][0]["text"]["content"] == papel
    )


def test_should_get_agents(mocker):
    # Mocks
    successResponse = mocker.Mock()
    successResponse.status = 200
    sample: str = (
        '{"object":"list","results":[{"object":"page","id":"4c65fc9c-2ff4-462e-9493-71ebb14c22cb","created_time":"2024-05-23T20:05:00.000Z","last_edited_time":"2024-05-23T20:18:00.000Z","created_by":{"object":"user","id":"6595192e-1c62-4f33-801c-84424f2ffa9c"},"last_edited_by":{"object":"user","id":"6595192e-1c62-4f33-801c-84424f2ffa9c"},"cover":null,"icon":{"type":"emoji","emoji":"👩🏻‍💻"},"parent":{"type":"database_id","database_id":"6301f640-e21c-4526-a72e-d96e7d4ba71d"},"archived":false,"in_trash":false,"properties":{"Papel":{"id":"PqtR","type":"rich_text","rich_text":[{"type":"text","text":{"content":"Desenvolvedor de Software com conhecimentos avançados em diferentes linguagens de programação como Python, C# e Java.","link":null},"annotations":{"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Desenvolvedor de Software com conhecimentos avançados em diferentes linguagens de programação como Python, C# e Java.","href":null}]},"Objetivo":{"id":"TF%7BM","type":"rich_text","rich_text":[{"type":"text","text":{"content":"Desenvolver códigos para solucionar problemas utilizando as tecnologias mais adequadas para cada caso","link":null},"annotations":{"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Desenvolver códigos para solucionar problemas utilizando as tecnologias mais adequadas para cada caso","href":null}]},"Nome":{"id":"title","type":"title","title":[{"type":"text","text":{"content":"Jasmine","link":null},"annotations":{"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Jasmine","href":null}]}},"url":"https://www.notion.so/Jasmine-4c65fc9c2ff4462e949371ebb14c22cb","public_url":null}],"next_cursor":null,"has_more":false,"type":"page_or_database","page_or_database":{},"developer_survey":"https://notionup.typeform.com/to/bllBsoI4?utm_source=postman","request_id":"1a76fec4-33aa-4137-901d-f163fe4c6042"}'
    )
    sample_bytes: bytes = sample.encode("utf-8")
    successResponse.read.return_value = sample_bytes
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
    assert response_data["results"].__len__() > 0
    assert "Nome" in response_data["results"][0]["properties"]
    assert "Objetivo" in response_data["results"][0]["properties"]
    assert "Papel" in response_data["results"][0]["properties"]


def test_should_get_agent_by_id(mocker):
    # Mocks
    successResponse = mocker.Mock()
    successResponse.status = 200
    sample: str = (
        '{"object":"page","id":"4c65fc9c-2ff4-462e-9493-71ebb14c22cb","created_time":"2024-05-23T20:05:00.000Z","last_edited_time":"2024-05-23T20:18:00.000Z","created_by":{"object":"user","id":"6595192e-1c62-4f33-801c-84424f2ffa9c"},"last_edited_by":{"object":"user","id":"6595192e-1c62-4f33-801c-84424f2ffa9c"},"cover":null,"icon":{"type":"emoji","emoji":"👩🏻‍💻"},"parent":{"type":"database_id","database_id":"6301f640-e21c-4526-a72e-d96e7d4ba71d"},"archived":false,"in_trash":false,"properties":{"Papel":{"id":"PqtR","type":"rich_text","rich_text":[{"type":"text","text":{"content":"Desenvolvedor de Software com conhecimentos avançados em diferentes linguagens de programação como Python, C# e Java.","link":null},"annotations":{"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Desenvolvedor de Software com conhecimentos avançados em diferentes linguagens de programação como Python, C# e Java.","href":null}]},"Objetivo":{"id":"TF%7BM","type":"rich_text","rich_text":[{"type":"text","text":{"content":"Desenvolver códigos para solucionar problemas utilizando as tecnologias mais adequadas para cada caso","link":null},"annotations":{"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Desenvolver códigos para solucionar problemas utilizando as tecnologias mais adequadas para cada caso","href":null}]},"Nome":{"id":"title","type":"title","title":[{"type":"text","text":{"content":"Jasmine","link":null},"annotations":{"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Jasmine","href":null}]}},"url":"https://www.notion.so/Jasmine-4c65fc9c2ff4462e949371ebb14c22cb","public_url":null,"developer_survey":"https://notionup.typeform.com/to/bllBsoI4?utm_source=postman","request_id":"423c5f03-26bc-47ed-b911-17e2a8a50b43"}'
    )
    successResponse.read.return_value = sample.encode("utf-8")
    conn = mocker.Mock()
    conn.getresponse.return_value = successResponse
    mocker.patch("http.client.HTTPSConnection", return_value=conn)

    # Arrange
    agent_id = "4c65fc9c-2ff4-462e-9493-71ebb14c22cb"

    # Act
    response_data: dict = agents_repository.get_agent_by_id(agent_id)

    # Assert
    assert response_data is not None
    assert "object" in response_data
    assert response_data["object"] == "page"
    assert "Nome" in response_data["properties"]
    assert "Objetivo" in response_data["properties"]
    assert "Papel" in response_data["properties"]


def test_should_get_agent_blocks(mocker):
    # Mocks
    successResponse = mocker.Mock()
    successResponse.status = 200
    sample: str = (
        '{"object":"list","results":[{"object":"block","id":"4dd595a3-bf18-4e14-938e-95a44ac77d72","parent":{"type":"page_id","page_id":"48a4c8b5-8c75-43ee-8863-505c38ffa20e"},"created_time":"2024-05-24T01:47:00.000Z","last_edited_time":"2024-05-24T01:47:00.000Z","created_by":{"object":"user","id":"27910b45-ae07-403c-b7e9-35b5adc896af"},"last_edited_by":{"object":"user","id":"27910b45-ae07-403c-b7e9-35b5adc896af"},"has_children":false,"archived":false,"in_trash":false,"type":"image","image":{"caption":[],"type":"external","external":{"url":"https://images.unsplash.com/photo-1513097633097-329a3a64e0d4?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb"}}}],"next_cursor":null,"has_more":false,"type":"block","block":{},"developer_survey":"https://notionup.typeform.com/to/bllBsoI4?utm_source=postman","request_id":"373070a3-4c10-4c76-bedb-d7b13357aa1e"}'
    )
    successResponse.read.return_value = sample.encode("utf-8")
    conn = mocker.Mock()
    conn.getresponse.return_value = successResponse
    mocker.patch("http.client.HTTPSConnection", return_value=conn)

    # Arrange
    agent_id = "4c65fc9c-2ff4-462e-9493-71ebb14c22cb"
    page_size = 100
    start_cursor = None

    # Act
    response_data: dict = agents_repository.get_agent_blocks(
        agent_id, page_size, start_cursor
    )

    # Assert
    assert response_data is not None
    assert "object" in response_data
    assert response_data["object"] == "list"
    assert "results" in response_data
    assert response_data["results"].__len__() > 0
    assert response_data["results"][0]["type"] == "image"
    assert "image" in response_data["results"][0]
    assert response_data["results"][0]["image"]["type"] == "external"
    assert response_data["results"][0]["image"]["external"]["url"] is not None


def test_should_get_agent_block_by_id(mocker):
    # Mocks
    successResponse = mocker.Mock()
    successResponse.status = 200
    sample: str = (
        '{"object":"block","id":"4dd595a3-bf18-4e14-938e-95a44ac77d72","parent":{"type":"page_id","page_id":"48a4c8b5-8c75-43ee-8863-505c38ffa20e"},"created_time":"2024-05-24T01:47:00.000Z","last_edited_time":"2024-05-24T01:47:00.000Z","created_by":{"object":"user","id":"27910b45-ae07-403c-b7e9-35b5adc896af"},"last_edited_by":{"object":"user","id":"27910b45-ae07-403c-b7e9-35b5adc896af"},"has_children":false,"archived":false,"in_trash":false,"type":"image","image":{"caption":[],"type":"external","external":{"url":"https://images.unsplash.com/photo-1513097633097-329a3a64e0d4?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb"}},"developer_survey":"https://notionup.typeform.com/to/bllBsoI4?utm_source=postman","request_id":"69311f8a-0570-45d6-ac3f-a4df15af4ef0"}'
    )
    successResponse.read.return_value = sample.encode("utf-8")
    conn = mocker.Mock()
    conn.getresponse.return_value = successResponse
    mocker.patch("http.client.HTTPSConnection", return_value=conn)

    # Arrange
    block_id = "4dd595a3-bf18-4e14-938e-95a44ac77d72"

    # Act
    response_data: dict = agents_repository.get_agent_block_by_id(block_id)

    # Assert
    assert response_data is not None
    assert "object" in response_data
    assert response_data["object"] == "block"
    assert "type" in response_data
    assert response_data["type"] == "image"
    assert "image" in response_data
    assert response_data["image"]["type"] == "external"
    assert "external" in response_data["image"]
    assert response_data["image"]["external"]["url"] is not None
