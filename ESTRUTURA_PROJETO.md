# Estrutura do Projeto AI Agents

## Diagrama de Árvore do Projeto

```
ai_agents/
├── .devcontainer/
│   ├── devcontainer.json          # Configuração do ambiente de desenvolvimento em container
│   └── provision.sh                # Script de provisionamento do ambiente
├── .vscode/
│   ├── launch.json                 # Configurações de debug do VS Code
│   └── settings.json               # Configurações do workspace VS Code
├── .env.dev.env                    # Variáveis de ambiente para desenvolvimento
├── .env.hml.env                    # Variáveis de ambiente para homologação
├── .env.prd.env                    # Variáveis de ambiente para produção
├── .gitignore                      # Arquivos ignorados pelo Git
├── Base.Dockerfile                 # Dockerfile base para build da aplicação
├── Jenkinsfile                     # Pipeline de CI/CD para Jenkins
├── README.md                       # Documentação principal do projeto
├── docker-build.sh                 # Script para build da imagem Docker
├── docker-run.sh                   # Script para executar o container Docker
├── requirements.txt                # Dependências Python do projeto
├── test-is-up.sh                   # Script de teste para verificar se a aplicação está rodando
│
├── main/                           # Código fonte principal
│   ├── ai_agents_library/          # Biblioteca específica do domínio de agentes
│   │   ├── __init__.py
│   │   ├── domain/                 # Camada de domínio (regras de negócio)
│   │   │   ├── __init__.py
│   │   │   ├── core/
│   │   │   └── models/
│   │   ├── repositories/           # Camada de acesso a dados
│   │   │   ├── __init__.py
│   │   │   ├── core/
│   │   │   │   └── agents_repository.py  # Repositório para gerenciar agentes no Notion
│   │   │   └── models/
│   │   ├── services/               # Camada de serviços (lógica de aplicação)
│   │   │   ├── __init__.py
│   │   │   ├── core/
│   │   │   └── models/
│   │   ├── tools/                  # Ferramentas específicas do domínio
│   │   │   ├── __init__.py
│   │   │   ├── core/
│   │   │   └── models/
│   │   └── utils/                  # Utilitários específicos do domínio
│   │       ├── __init__.py
│   │       ├── core/
│   │       └── models/
│   │
│   ├── entrypoint/                 # Ponto de entrada da aplicação
│   │   ├── __init__.py
│   │   ├── main.py                 # Arquivo principal que inicia a API FastAPI
│   │   └── controllers/            # Controladores REST API
│   │       ├── __init__.py
│   │       └── main_controller.py  # Controller com endpoints CRUD de exemplo
│   │
│   └── library/                    # Biblioteca genérica reutilizável
│       ├── __init__.py
│       ├── di_container.py         # Container de injeção de dependências
│       ├── repositories/
│       │   └── __init__.py
│       ├── services/
│       │   └── __init__.py
│       ├── tools/                  # Ferramentas genéricas
│       │   ├── __init__.py
│       │   └── core/
│       │       ├── http_client_tool.py    # Cliente HTTP
│       │       ├── log_tool.py            # Ferramenta de logging
│       │       └── settings_tool.py       # Gerenciador de configurações
│       └── utils/                  # Utilitários genéricos
│           ├── __init__.py
│           ├── core/
│           │   ├── path_helper.py         # Auxiliar para paths
│           │   └── settings_helper.py     # Auxiliar para configurações
│           └── models/
│               └── validation_exception.py # Exceção customizada
│
└── tests/                          # Testes automatizados
    ├── __init__.py
    ├── ai_agents_library/          # Testes da biblioteca de agentes
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
    └── library/                    # Testes da biblioteca genérica
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

## Sobre o Projeto

### Descrição Geral

**AI Agents** é um **simulador de agentes via IA generativa** - um microsserviço Python que fornece uma infraestrutura robusta para gerenciar e simular agentes de IA. O projeto implementa uma API RESTful usando FastAPI para criar, ler, atualizar e deletar informações sobre agentes que são armazenados no Notion.

### Propósito

O sistema foi projetado para:
- **Gerenciar Agentes de IA**: Criar e gerenciar perfis de agentes com nome, papel e objetivo
- **Integração com Notion**: Utiliza a API do Notion como banco de dados para armazenar informações dos agentes
- **Simulação de Agentes**: Fornecer uma base para simulação de comportamentos de agentes via IA generativa

### Arquitetura

O projeto segue uma **arquitetura em camadas limpa** (Clean Architecture) com separação clara de responsabilidades:

#### 1. **Camada de Entrypoint (entrypoint/)**
- Ponto de entrada da aplicação
- Contém a configuração do FastAPI e os controladores REST
- `main.py`: Inicializa o servidor web Uvicorn na porta 8000
- `main_controller.py`: Endpoints REST para operações CRUD

#### 2. **Camada de Domínio (ai_agents_library/)**
- **Domain**: Regras de negócio e entidades do domínio
- **Repositories**: Acesso a dados externos (integração com Notion API)
  - `agents_repository.py`: Gerencia operações CRUD de agentes no Notion
- **Services**: Lógica de aplicação e orquestração
- **Tools**: Ferramentas específicas do domínio
- **Utils**: Utilitários específicos do domínio

#### 3. **Camada de Biblioteca Genérica (library/)**
- Código reutilizável e independente do domínio
- **di_container.py**: Gerenciamento de injeção de dependências usando `dependency-injector`
- **Tools**:
  - `log_tool.py`: Sistema de logging com níveis (INFO, WARN, ERROR)
  - `settings_tool.py`: Gerenciamento de configurações por ambiente
  - `http_client_tool.py`: Cliente HTTP genérico
- **Utils**:
  - `settings_helper.py`: Carregamento de variáveis de ambiente
  - `path_helper.py`: Manipulação de caminhos de arquivos

#### 4. **Camada de Testes (tests/)**
- Testes unitários usando pytest
- Espelha a estrutura do código fonte
- Usa pytest-mock para mocking

### Tecnologias Utilizadas

```python
# Principais dependências (requirements.txt)
fastapi==0.109.2           # Framework web assíncrono
uvicorn==0.27.1            # Servidor ASGI
httpx==0.26.0              # Cliente HTTP assíncrono
dependency-injector==4.41.0 # Injeção de dependências
python-dotenv==1.0.1       # Gerenciamento de variáveis de ambiente
pytest==8.0.0              # Framework de testes
pytest-mock==3.14.0        # Mocking para testes
```

### Funcionalidades da API

#### Endpoints Disponíveis:

1. **GET /info**
   - Retorna informações do microsserviço (nome, versão, sistema operacional, Python version, ambiente)

2. **POST /create**
   - Cria um novo objeto (exemplo genérico de CRUD)

3. **GET /read/{id}**
   - Lê um objeto por ID

4. **PUT /update/{id}**
   - Atualiza um objeto existente

5. **DELETE /delete/{id}**
   - Remove um objeto

### Integração com Notion

O sistema utiliza a **API do Notion** como banco de dados para armazenar informações dos agentes:

**Configurações necessárias (.env.*.env):**
```bash
NOTION_PROTOCOL="https"
NOTION_HOST="api.notion.com"
NOTION_PORT="443"
NOTION_VERSION="2022-02-22"
NOTION_API_KEY="secret_123"        # Chave de API do Notion
NOTION_AGENTS_DB_ID="database_123"  # ID do banco de dados de agentes
```

**Funcionalidades do AgentsRepository:**
- `create_agent()`: Cria novo agente no Notion com nome, papel, objetivo e imagem
- `get_agents()`: Lista agentes com paginação
- `get_agent_by_id()`: Busca agente específico
- `get_agent_blocks()`: Obtém blocos de conteúdo de um agente
- `get_agent_block_by_id()`: Busca bloco específico

### Ambientes

O projeto suporta **três ambientes**:
- **dev** (desenvolvimento): `.env.dev.env`
- **hml** (homologação): `.env.hml.env`
- **prd** (produção): `.env.prd.env`

### Deploy e CI/CD

#### Docker
- **Base.Dockerfile**: Imagem base Python 3.11 com dependências instaladas
- **docker-build.sh**: Script para construir a imagem Docker
- **docker-run.sh**: Script para executar o container na porta 8000

#### Jenkins Pipeline
O **Jenkinsfile** define um pipeline com 3 estágios:
1. **Build**: Constrói a imagem Docker
2. **Run**: Executa o container
3. **Test**: Verifica se a aplicação está respondendo

### Como Executar

#### Localmente:
```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar ambiente
export MICRO_TOOLS_SYS_ENV=dev

# Executar aplicação
python main/entrypoint/main.py
```

#### Com Docker:
```bash
# Build
bash docker-build.sh

# Run
bash docker-run.sh

# Test
bash test-is-up.sh
```

A aplicação estará disponível em: http://localhost:8000

Documentação Swagger disponível em: http://localhost:8000/docs

### Padrões de Código

- **Injeção de Dependências**: Uso extensivo de DI para desacoplamento
- **Type Hints**: Tipagem estática Python para melhor manutenibilidade
- **Logging Estruturado**: Sistema de logs com diferentes níveis
- **Tratamento de Erros**: Exceções customizadas e tratamento adequado
- **Testes Automatizados**: Cobertura de testes com pytest

### Estrutura Modular

O projeto é altamente modular e desacoplado:
- **library/**: Código genérico reutilizável em qualquer projeto
- **ai_agents_library/**: Código específico do domínio de agentes de IA
- **entrypoint/**: Camada de apresentação (API REST)
- **tests/**: Testes espelhando a estrutura do código

Esta separação permite:
- Reutilização de código
- Facilidade de manutenção
- Testabilidade
- Evolução independente de cada camada
