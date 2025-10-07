# AI Agents

Simulador de agentes via IA generativa

## Descrição

**AI Agents** é um microsserviço Python desenvolvido com FastAPI que fornece uma infraestrutura robusta para gerenciar e simular agentes de IA. O sistema utiliza a API do Notion como banco de dados para armazenar informações dos agentes (nome, papel, objetivo e imagem).

## Características Principais

- 🤖 **Gerenciamento de Agentes de IA**: CRUD completo para agentes via API REST
- 📝 **Integração com Notion**: Utiliza Notion como banco de dados
- 🏗️ **Arquitetura Limpa**: Separação em camadas (Entrypoint, Domain, Library)
- 💉 **Injeção de Dependências**: Usando dependency-injector
- 🧪 **Testes Automatizados**: Cobertura com pytest
- 🐳 **Containerização**: Pronto para Docker e CI/CD
- 📚 **Documentação OpenAPI**: Swagger UI disponível em `/docs`

## Documentação Detalhada / Detailed Documentation

Para uma explicação completa da estrutura do projeto, arquitetura e funcionamento, consulte:

📖 **[ESTRUTURA_PROJETO.md](ESTRUTURA_PROJETO.md)** (Português) - Documentação detalhada com:
- Diagrama completo da árvore de arquivos e pastas
- Explicação da arquitetura em camadas
- Descrição de cada componente
- Tecnologias utilizadas
- Instruções de deploy e execução

📖 **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** (English) - Detailed documentation with:
- Complete file and folder tree diagram
- Layered architecture explanation
- Component descriptions
- Technologies used
- Deployment and execution instructions

## Início Rápido

### Requisitos
- Python 3.11+
- Docker (opcional)

### Instalação Local

```bash
# Clonar o repositório
git clone https://github.com/lsilvpin/ai_agents.git
cd ai_agents

# Instalar dependências
pip install -r requirements.txt

# Configurar ambiente
export MICRO_TOOLS_SYS_ENV=dev

# Executar aplicação
python main/entrypoint/main.py
```

### Executar com Docker

```bash
# Build da imagem
bash docker-build.sh

# Executar container
bash docker-run.sh

# Testar se está funcionando
bash test-is-up.sh
```

## Endpoints da API

A aplicação estará disponível em `http://localhost:8000`

- **GET** `/info` - Informações do microsserviço
- **POST** `/create` - Criar novo objeto
- **GET** `/read/{id}` - Ler objeto por ID
- **PUT** `/update/{id}` - Atualizar objeto
- **DELETE** `/delete/{id}` - Deletar objeto

Acesse a documentação interativa em: `http://localhost:8000/docs`

## Configuração

Configure as variáveis de ambiente nos arquivos:
- `.env.dev.env` - Desenvolvimento
- `.env.hml.env` - Homologação  
- `.env.prd.env` - Produção

### Variáveis Necessárias

```bash
sys_name="ai_agents"
log_level="debug"
NOTION_PROTOCOL="https"
NOTION_HOST="api.notion.com"
NOTION_PORT="443"
NOTION_VERSION="2022-02-22"
NOTION_API_KEY="your_notion_api_key"
NOTION_AGENTS_DB_ID="your_notion_database_id"
```

## Testes

```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=main
```

## Estrutura do Projeto

```
ai_agents/
├── main/                    # Código fonte
│   ├── ai_agents_library/   # Domínio específico de agentes
│   ├── entrypoint/          # API REST (FastAPI)
│   └── library/             # Biblioteca genérica reutilizável
├── tests/                   # Testes automatizados
├── requirements.txt         # Dependências Python
└── Base.Dockerfile          # Container Docker
```

Para mais detalhes, veja:
- [ESTRUTURA_PROJETO.md](ESTRUTURA_PROJETO.md) (Português)
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) (English)

## Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **Uvicorn** - Servidor ASGI
- **Pytest** - Framework de testes
- **Dependency Injector** - Injeção de dependências
- **Python-dotenv** - Gerenciamento de configurações
- **Docker** - Containerização

## CI/CD

Pipeline Jenkins configurado com 3 estágios:
1. Build - Construir imagem Docker
2. Run - Executar container
3. Test - Validar funcionamento

## Licença

Este projeto está sob licença MIT.

## Autor

[lsilvpin](https://github.com/lsilvpin)
