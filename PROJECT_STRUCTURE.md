# AI Agents Project Structure

## Project Tree Diagram

```
ai_agents/
├── .devcontainer/
│   ├── devcontainer.json          # Dev container environment configuration
│   └── provision.sh                # Environment provisioning script
├── .vscode/
│   ├── launch.json                 # VS Code debug configurations
│   └── settings.json               # VS Code workspace settings
├── .env.dev.env                    # Development environment variables
├── .env.hml.env                    # Staging environment variables
├── .env.prd.env                    # Production environment variables
├── .gitignore                      # Git ignored files
├── Base.Dockerfile                 # Base Dockerfile for application build
├── Jenkinsfile                     # CI/CD pipeline for Jenkins
├── README.md                       # Main project documentation
├── docker-build.sh                 # Script to build Docker image
├── docker-run.sh                   # Script to run Docker container
├── requirements.txt                # Python project dependencies
├── test-is-up.sh                   # Test script to verify application is running
│
├── main/                           # Main source code
│   ├── ai_agents_library/          # Domain-specific agents library
│   │   ├── __init__.py
│   │   ├── domain/                 # Domain layer (business rules)
│   │   │   ├── __init__.py
│   │   │   ├── core/
│   │   │   └── models/
│   │   ├── repositories/           # Data access layer
│   │   │   ├── __init__.py
│   │   │   ├── core/
│   │   │   │   └── agents_repository.py  # Repository to manage agents in Notion
│   │   │   └── models/
│   │   ├── services/               # Service layer (application logic)
│   │   │   ├── __init__.py
│   │   │   ├── core/
│   │   │   └── models/
│   │   ├── tools/                  # Domain-specific tools
│   │   │   ├── __init__.py
│   │   │   ├── core/
│   │   │   └── models/
│   │   └── utils/                  # Domain-specific utilities
│   │       ├── __init__.py
│   │       ├── core/
│   │       └── models/
│   │
│   ├── entrypoint/                 # Application entry point
│   │   ├── __init__.py
│   │   ├── main.py                 # Main file that starts the FastAPI application
│   │   └── controllers/            # REST API controllers
│   │       ├── __init__.py
│   │       └── main_controller.py  # Controller with sample CRUD endpoints
│   │
│   └── library/                    # Generic reusable library
│       ├── __init__.py
│       ├── di_container.py         # Dependency injection container
│       ├── repositories/
│       │   └── __init__.py
│       ├── services/
│       │   └── __init__.py
│       ├── tools/                  # Generic tools
│       │   ├── __init__.py
│       │   └── core/
│       │       ├── http_client_tool.py    # HTTP client
│       │       ├── log_tool.py            # Logging tool
│       │       └── settings_tool.py       # Configuration manager
│       └── utils/                  # Generic utilities
│           ├── __init__.py
│           ├── core/
│           │   ├── path_helper.py         # Path helper
│           │   └── settings_helper.py     # Settings helper
│           └── models/
│               └── validation_exception.py # Custom exception
│
└── tests/                          # Automated tests
    ├── __init__.py
    ├── ai_agents_library/          # Agents library tests
    │   ├── __init__.py
    │   ├── domain/
    │   ├── repositories/
    │   │   └── core/
    │   │       └── agents_repository_test.py
    │   ├── services/
    │   ├── tools/
    │   └── utils/
    ├── entrypoint/
    │   └── controllers/
    │       └── main_controller_test.py
    └── library/                    # Generic library tests
        ├── repositories/
        ├── services/
        ├── tools/
        │   └── core/
        │       ├── http_client_tool_test.py
        │       ├── log_tool_test.py
        │       └── settings_tool_test.py
        └── utils/
            └── core/
                ├── path_helper_test.py
                └── settings_helper_test.py
```

## About the Project

### Overview

**AI Agents** is an **AI Agent Simulator via Generative AI** - a Python microservice that provides a robust infrastructure for managing and simulating AI agents. The project implements a RESTful API using FastAPI to create, read, update, and delete information about agents stored in Notion.

### Purpose

The system is designed to:
- **Manage AI Agents**: Create and manage agent profiles with name, role, and objective
- **Notion Integration**: Uses the Notion API as a database to store agent information
- **Agent Simulation**: Provide a foundation for simulating agent behaviors via generative AI

### Architecture

The project follows a **Clean Architecture** layered approach with clear separation of concerns:

#### 1. **Entrypoint Layer (entrypoint/)**
- Application entry point
- Contains FastAPI configuration and REST controllers
- `main.py`: Initializes Uvicorn web server on port 8000
- `main_controller.py`: REST endpoints for CRUD operations

#### 2. **Domain Layer (ai_agents_library/)**
- **Domain**: Business rules and domain entities
- **Repositories**: External data access (Notion API integration)
  - `agents_repository.py`: Manages agent CRUD operations in Notion
- **Services**: Application logic and orchestration
- **Tools**: Domain-specific tools
- **Utils**: Domain-specific utilities

#### 3. **Generic Library Layer (library/)**
- Reusable, domain-independent code
- **di_container.py**: Dependency injection management using `dependency-injector`
- **Tools**:
  - `log_tool.py`: Logging system with levels (INFO, WARN, ERROR)
  - `settings_tool.py`: Environment-based configuration management
  - `http_client_tool.py`: Generic HTTP client
- **Utils**:
  - `settings_helper.py`: Environment variable loading
  - `path_helper.py`: File path manipulation

#### 4. **Test Layer (tests/)**
- Unit tests using pytest
- Mirrors source code structure
- Uses pytest-mock for mocking

### Technologies Used

```python
# Main dependencies (requirements.txt)
fastapi==0.109.2           # Asynchronous web framework
uvicorn==0.27.1            # ASGI server
httpx==0.26.0              # Asynchronous HTTP client
dependency-injector==4.41.0 # Dependency injection
python-dotenv==1.0.1       # Environment variable management
pytest==8.0.0              # Testing framework
pytest-mock==3.14.0        # Mocking for tests
```

### API Features

#### Available Endpoints:

1. **GET /info**
   - Returns microservice information (name, version, OS, Python version, environment)

2. **POST /create**
   - Creates a new object (generic CRUD example)

3. **GET /read/{id}**
   - Reads an object by ID

4. **PUT /update/{id}**
   - Updates an existing object

5. **DELETE /delete/{id}**
   - Removes an object

### Notion Integration

The system uses the **Notion API** as a database to store agent information:

**Required configurations (.env.*.env):**
```bash
NOTION_PROTOCOL="https"
NOTION_HOST="api.notion.com"
NOTION_PORT="443"
NOTION_VERSION="2022-02-22"
NOTION_API_KEY="secret_123"        # Notion API key
NOTION_AGENTS_DB_ID="database_123"  # Agents database ID
```

**AgentsRepository Features:**
- `create_agent()`: Creates new agent in Notion with name, role, objective, and image
- `get_agents()`: Lists agents with pagination
- `get_agent_by_id()`: Fetches specific agent
- `get_agent_blocks()`: Gets content blocks from an agent
- `get_agent_block_by_id()`: Fetches specific block

### Environments

The project supports **three environments**:
- **dev** (development): `.env.dev.env`
- **hml** (staging): `.env.hml.env`
- **prd** (production): `.env.prd.env`

### Deployment and CI/CD

#### Docker
- **Base.Dockerfile**: Python 3.11 base image with dependencies installed
- **docker-build.sh**: Script to build Docker image
- **docker-run.sh**: Script to run container on port 8000

#### Jenkins Pipeline
The **Jenkinsfile** defines a pipeline with 3 stages:
1. **Build**: Builds Docker image
2. **Run**: Runs container
3. **Test**: Verifies application is responding

### How to Run

#### Locally:
```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
export MICRO_TOOLS_SYS_ENV=dev

# Run application
python main/entrypoint/main.py
```

#### With Docker:
```bash
# Build
bash docker-build.sh

# Run
bash docker-run.sh

# Test
bash test-is-up.sh
```

The application will be available at: http://localhost:8000

Swagger documentation available at: http://localhost:8000/docs

### Code Patterns

- **Dependency Injection**: Extensive use of DI for decoupling
- **Type Hints**: Python static typing for better maintainability
- **Structured Logging**: Log system with different levels
- **Error Handling**: Custom exceptions and proper handling
- **Automated Testing**: Test coverage with pytest

### Modular Structure

The project is highly modular and decoupled:
- **library/**: Generic code reusable in any project
- **ai_agents_library/**: AI agents domain-specific code
- **entrypoint/**: Presentation layer (REST API)
- **tests/**: Tests mirroring code structure

This separation enables:
- Code reusability
- Easy maintenance
- Testability
- Independent evolution of each layer

## Key Components

### AgentsRepository
Manages all interactions with the Notion API for agent data:
- Creates agents with metadata (name, role, objective, image)
- Queries agent database with pagination support
- Retrieves individual agent details
- Fetches agent content blocks

### Dependency Injection Container
Centralizes dependency management:
- LogTool: For logging across the application
- SettingsTool: For configuration management
- HttpClientTool: For HTTP requests
- AgentsRepository: For Notion API interactions

### Settings Management
Multi-environment configuration system:
- Environment-based config files (dev/hml/prd)
- Settings loaded via python-dotenv
- Centralized access through SettingsTool and settings_helper

### Logging System
Structured logging with three levels:
- INFO: Informational messages
- WARN: Warning messages
- ERROR: Error messages (logged to stderr)

## Development Guidelines

### Adding New Features
1. Define domain models in `ai_agents_library/domain/models/`
2. Implement business logic in `ai_agents_library/services/core/`
3. Create repository methods in `ai_agents_library/repositories/core/`
4. Add API endpoints in `entrypoint/controllers/`
5. Write tests mirroring the structure in `tests/`

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=main

# Run specific test file
pytest tests/library/tools/core/log_tool_test.py
```

### Docker Development
```bash
# Build image
docker build -f Base.Dockerfile -t ai_agents:dev .

# Run container
docker run -p 8000:8000 ai_agents:dev uvicorn main.entrypoint.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once the application is running, interactive API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Configuration

Each environment file (`.env.*.env`) should contain:
```bash
sys_name="ai_agents"           # System name
log_level="debug"              # Log level (debug/warning/error)
NOTION_PROTOCOL="https"        # Notion API protocol
NOTION_HOST="api.notion.com"   # Notion API host
NOTION_PORT="443"              # Notion API port
NOTION_VERSION="2022-02-22"    # Notion API version
NOTION_API_KEY="your_key"      # Your Notion integration API key
NOTION_AGENTS_DB_ID="your_db"  # Your Notion database ID
```

## License

This project is licensed under the MIT License.

## Author

[lsilvpin](https://github.com/lsilvpin)
