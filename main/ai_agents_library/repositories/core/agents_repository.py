import json
import os, sys, http.client

sys.path.insert(0, os.path.abspath("."))
from main.library.tools.core.log_tool import LogTool
from main.library.tools.core.settings_tool import SettingsTool


class AgentsRepository:
    def __init__(self, settings_tool: SettingsTool, log_tool: LogTool):
        self.settings_tool = settings_tool
        self.log_tool = log_tool

    def create_agent(
        self, nome: str, papel: str, objetivo: str, image_url: str
    ) -> dict:
        assert nome is not None, "Nome cannot be None"
        assert papel is not None, "Papel cannot be None"
        assert objetivo is not None, "Objetivo cannot be None"
        assert image_url is not None, "Image URL cannot be None"
        notion_protocol: str = self.settings_tool.get("NOTION_PROTOCOL")
        assert notion_protocol is not None, "NOTION_PROTOCOL cannot be None"
        notion_host: str = self.settings_tool.get("NOTION_HOST")
        assert notion_host is not None, "NOTION_HOST cannot be None"
        notion_port: str = self.settings_tool.get("NOTION_PORT")
        assert notion_port is not None, "NOTION_PORT cannot be None"
        notion_version: str = self.settings_tool.get("NOTION_VERSION")
        assert notion_version is not None, "NOTION_VERSION cannot be None"
        notion_api_key: str = self.settings_tool.get("NOTION_API_KEY")
        assert notion_api_key is not None, "NOTION_API_KEY cannot be None"
        notion_database_id: str = self.settings_tool.get("NOTION_AGENTS_DB_ID")
        assert notion_database_id is not None, "NOTION_DATABASE_ID cannot be None"
        notion_database_uri: str = f"/v1/pages"
        headers: dict = {
            "Authorization": f"Bearer {notion_api_key}",
            "Content-Type": "application/json",
            "Notion-Version": notion_version,
        }
        body: dict = {
            "parent": {"database_id": notion_database_id},
            "icon": {"type": "emoji", "emoji": "👩🏻‍💻"},
            "properties": {
                "Nome": {
                    "title": [
                        {
                            "text": {
                                "content": nome,
                            }
                        }
                    ]
                },
                "Papel": {
                    "rich_text": [
                        {
                            "text": {
                                "content": papel,
                            }
                        }
                    ]
                },
                "Objetivo": {
                    "rich_text": [
                        {
                            "text": {
                                "content": objetivo,
                            }
                        }
                    ]
                },
            },
            "children": [
                {
                    "object": "block",
                    "type": "image",
                    "image": {
                        "caption": [],
                        "type": "external",
                        "external": {
                            "url": image_url,
                        },
                    },
                }
            ],
        }
        body_json: str = json.dumps(body)
        isHttps: bool = notion_protocol == "https"
        conn: http.client.HTTPSConnection = (
            http.client.HTTPSConnection(notion_host, notion_port)
            if isHttps
            else http.client.HTTPConnection(notion_host, notion_port)
        )
        assert conn is not None, "Connection cannot be None"
        conn.request("POST", notion_database_uri, body_json, headers)
        response: http.client.HTTPResponse = conn.getresponse()
        assert response is not None, "Response cannot be None"
        response_status: int = response.status
        response_data: bytes = response.read()
        self.__validate_response(response_status, response.reason, response_data)
        response_str: str = response_data.decode("utf-8")
        response_dict: dict = json.loads(response_str)
        return response_dict

    def get_agents(
        self, page_size: int = 100, start_cursor: str | None = None, body: dict | None = None
    ) -> dict:
        notion_protocol: str = self.settings_tool.get("NOTION_PROTOCOL")
        assert notion_protocol is not None, "NOTION_PROTOCOL cannot be None"
        notion_host: str = self.settings_tool.get("NOTION_HOST")
        assert notion_host is not None, "NOTION_HOST cannot be None"
        notion_port: str = self.settings_tool.get("NOTION_PORT")
        assert notion_port is not None, "NOTION_PORT cannot be None"
        notion_version: str = self.settings_tool.get("NOTION_VERSION")
        assert notion_version is not None, "NOTION_VERSION cannot be None"
        notion_api_key: str = self.settings_tool.get("NOTION_API_KEY")
        assert notion_api_key is not None, "NOTION_API_KEY cannot be None"
        notion_database_id: str = self.settings_tool.get("NOTION_AGENTS_DB_ID")
        assert notion_database_id is not None, "NOTION_DATABASE_ID cannot be None"
        notion_database_query_uri: str = f"/v1/databases/{notion_database_id}/query"
        headers: dict = {
            "Authorization": f"Bearer {notion_api_key}",
            "Notion-Version": notion_version,
        }
        if not body:
            body = {
                "page_size": page_size,
            }
        else:
            assert "page_size" in body, "Page size must be in the body"
        if start_cursor:
            body["start_cursor"] = start_cursor
        body_json: str = json.dumps(body)
        isHttps: bool = notion_protocol == "https"
        conn: http.client.HTTPSConnection = (
            http.client.HTTPSConnection(notion_host, notion_port)
            if isHttps
            else http.client.HTTPConnection(notion_host, notion_port)
        )
        assert conn is not None, "Connection cannot be None"
        conn.request("POST", notion_database_query_uri, body_json, headers)
        response: http.client.HTTPResponse = conn.getresponse()
        assert response is not None, "Response cannot be None"
        response_status: int = response.status
        response_data: bytes = response.read()
        self.__validate_response(response_status, response.reason, response_data)
        response_str: str = response_data.decode("utf-8")
        response_dict: dict = json.loads(response_str)
        return response_dict

    def get_agent_by_id(self, agent_id: str) -> dict:
        notion_protocol: str = self.settings_tool.get("NOTION_PROTOCOL")
        assert notion_protocol is not None, "NOTION_PROTOCOL cannot be None"
        notion_host: str = self.settings_tool.get("NOTION_HOST")
        assert notion_host is not None, "NOTION_HOST cannot be None"
        notion_port: str = self.settings_tool.get("NOTION_PORT")
        assert notion_port is not None, "NOTION_PORT cannot be None"
        notion_version: str = self.settings_tool.get("NOTION_VERSION")
        assert notion_version is not None, "NOTION_VERSION cannot be None"
        notion_api_key: str = self.settings_tool.get("NOTION_API_KEY")
        assert notion_api_key is not None, "NOTION_API_KEY cannot be None"
        notion_database_id: str = self.settings_tool.get("NOTION_AGENTS_DB_ID")
        assert notion_database_id is not None, "NOTION_DATABASE_ID cannot be None"
        notion_database_uri: str = f"/v1/pages/{agent_id}"
        headers: dict = {
            "Authorization": f"Bearer {notion_api_key}",
            "Notion-Version": notion_version,
        }
        isHttps: bool = notion_protocol == "https"
        conn: http.client.HTTPSConnection = (
            http.client.HTTPSConnection(notion_host, notion_port)
            if isHttps
            else http.client.HTTPConnection(notion_host, notion_port)
        )
        assert conn is not None, "Connection cannot be None"
        conn.request("GET", notion_database_uri, headers=headers)
        response: http.client.HTTPResponse = conn.getresponse()
        assert response is not None, "Response cannot be None"
        response_status: int = response.status
        response_data: bytes = response.read()
        self.__validate_response(response_status, response.reason, response_data)
        response_str: str = response_data.decode("utf-8")
        response_dict: dict = json.loads(response_str)
        return response_dict

    def get_agent_blocks(
        self, agent_id: str, page_size: int = 100, start_cursor: str | None = None
    ) -> dict:
        assert agent_id is not None, "Agent ID cannot be None"
        assert page_size > 0, "Page size must be greater than 0"
        notion_protocol: str = self.settings_tool.get("NOTION_PROTOCOL")
        assert notion_protocol is not None, "NOTION_PROTOCOL cannot be None"
        notion_host: str = self.settings_tool.get("NOTION_HOST")
        assert notion_host is not None, "NOTION_HOST cannot be None"
        notion_port: str = self.settings_tool.get("NOTION_PORT")
        assert notion_port is not None, "NOTION_PORT cannot be None"
        notion_version: str = self.settings_tool.get("NOTION_VERSION")
        assert notion_version is not None, "NOTION_VERSION cannot be None"
        notion_api_key: str = self.settings_tool.get("NOTION_API_KEY")
        assert notion_api_key is not None, "NOTION_API_KEY cannot be None"
        notion_database_id: str = self.settings_tool.get("NOTION_AGENTS_DB_ID")
        assert notion_database_id is not None, "NOTION_DATABASE_ID cannot be None"
        notion_database_uri: str = f"/v1/blocks/{agent_id}/children?page_size={page_size}"
        if start_cursor:
            notion_database_uri += f"&start_cursor={start_cursor}"
        headers: dict = {
            "Authorization": f"Bearer {notion_api_key}",
            "Notion-Version": notion_version,
        }
        isHttps: bool = notion_protocol == "https"
        conn: http.client.HTTPSConnection = (
            http.client.HTTPSConnection(notion_host, notion_port)
            if isHttps
            else http.client.HTTPConnection(notion_host, notion_port)
        )
        assert conn is not None, "Connection cannot be None"
        conn.request("GET", notion_database_uri, headers=headers)
        response: http.client.HTTPResponse = conn.getresponse()
        assert response is not None, "Response cannot be None"
        response_status: int = response.status
        response_data: bytes = response.read()
        self.__validate_response(response_status, response.reason, response_data)
        response_str: str = response_data.decode("utf-8")
        response_dict: dict = json.loads(response_str)
        return response_dict

    def __validate_response(self, status_code: int, reason: str, response_data: bytes):
        if status_code < 200:
            if reason is not None and reason != "":
                if response_data is not None and response_data != b"":
                    raise Exception(
                        f"Request failed with status code {status_code}, reason {reason}, and response data {response_data}"
                    )
                else:
                    raise Exception(
                        f"Request failed with status code {status_code} and reason {reason}"
                    )
            else:
                raise Exception(f"Request failed with status code {status_code}")
