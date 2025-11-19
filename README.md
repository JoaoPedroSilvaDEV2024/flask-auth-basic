# API de Autenticação com Flask e JWT

Uma API segura de autenticação construída com Flask e JSON Web Tokens (JWT). Esta API fornece endpoints para registro de usuários, login e acesso a rotas protegidas por token, ideal como base para aplicações web e mobile que precisam de autenticação baseada em tokens.

---

## Índice

- [Descrição](#descrição)
- [Objetivo do projeto](#objetivo-do-projeto)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração (variáveis de ambiente)](#configuração-variáveis-de-ambiente)
- [Como rodar](#como-rodar)
- [Endpoints disponíveis](#endpoints-disponíveis)
- [Exemplos de requisições JSON](#exemplos-de-requisições-json)
- [Estrutura de pastas do projeto](#estrutura-de-pastas-do-projeto)
- [Boas práticas e notas de segurança](#boas-práticas-e-notas-de-segurança)
- [Contato](#contato)

---

## Descrição

Esta API demonstra uma implementação típica de autenticação usando Flask (microframework Python) com JWT para emissão de tokens que autenticam acesso a rotas protegidas. O propósito é ser clara, modular e fácil de adaptar para projetos reais.

---

## Objetivo do projeto

- Fornecer uma base simples e segura para autenticação de usuários usando JWT.
- Servir como exemplo para aprender a integrar Flask com autenticação por tokens.
- Ser facilmente extensível (ex.: refresh tokens, roles, integração com OAuth, persistência avançada).

---

## Tecnologias utilizadas

- Python 3.8+
- Flask
- Flask-JWT-Extended (ou biblioteca JWT equivalente)
- Flask-SQLAlchemy (ou outra camada de persistência)
- SQLite (exemplo) — pode ser substituído por PostgreSQL, MySQL, etc.
- pip / virtualenv

---

## Pré-requisitos

- Python 3.8 ou superior
- pip
- virtualenv (opcional, recomendado)

---

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/JoaoPedroSilvaDEV2024/seu-repo-de-login-flask-jwt.git
cd seu-repo-de-login-flask-jwt
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

(Se você não tiver um `requirements.txt`, instale manualmente:)
```bash
pip install Flask Flask-JWT-Extended Flask-SQLAlchemy
```

---

## Configuração (variáveis de ambiente)

Crie um arquivo `.env` ou exporte as variáveis diretamente no ambiente:

- FLASK_APP: nome do módulo principal (ex.: app.py)
- FLASK_ENV: development (opcional)
- SECRET_KEY: chave secreta do Flask (para sessões, CSRF se aplicável)
- JWT_SECRET_KEY: chave secreta usada para assinar os JWTs
- DATABASE_URL: URI do banco de dados (ex.: sqlite:///instance/app.db)

Exemplo `.env`:
```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=sua_secret_key_forte
JWT_SECRET_KEY=sua_jwt_secret_key_muito_forte
DATABASE_URL=sqlite:///instance/app.db
```

Nunca comite chaves secretas em repositórios públicos.

---

## Como rodar

1. Configure variáveis de ambiente (veja seção anterior).
2. Execute as migrations (se usar Flask-Migrate) ou crie o banco:
```bash
# exemplo simples sem migrations:
python -c "from app import db; db.create_all()"
```

3. Inicie a aplicação:
```bash
flask run
# ou
python app.py
```

Por padrão, a aplicação ficará disponível em `http://127.0.0.1:5000`.

---

## Endpoints disponíveis

Abaixo estão os endpoints típicos dessa API. Ajuste os nomes/rotas conforme sua implementação.

- POST /register
  - Descrição: Registra um novo usuário.
  - Corpo: JSON (email, senha, nome).
  - Resposta: Mensagem de sucesso ou erro.

- POST /login
  - Descrição: Realiza autenticação e retorna um access token (JWT).
  - Corpo: JSON (email, senha).
  - Resposta: JSON com token (ex.: access_token).

- GET /protected
  - Descrição: Exemplo de rota protegida. Requer header Authorization com Bearer token.
  - Cabeçalho: Authorization: Bearer <access_token>
  - Resposta: Conteúdo protegido (ex.: dados do usuário).

- (Opcional) POST /refresh
  - Descrição: Gera um novo access token usando um refresh token (se implementado).

- (Opcional) POST /logout
  - Descrição: Invalida token (se integrar blacklist/revocation).

---

## Exemplos de requisições JSON

1) Registro (POST /register)
Request:
```json
POST /register
Content-Type: application/json

{
  "email": "usuario@example.com",
  "password": "SenhaSegura123!",
  "name": "João Silva"
}
```

Resposta de sucesso (exemplo):
```json
{
  "message": "Usuário criado com sucesso",
  "user": {
    "id": 1,
    "email": "usuario@example.com",
    "name": "João Silva"
  }
}
```

2) Login (POST /login)
Request:
```json
POST /login
Content-Type: application/json

{
  "email": "usuario@example.com",
  "password": "SenhaSegura123!"
}
```

Resposta de sucesso (exemplo):
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

3) Acessando rota protegida (GET /protected)
Request:
```
GET /protected
Authorization: Bearer <access_token_aqui>
```

Resposta de sucesso (exemplo):
```json
{
  "message": "Acesso autorizado",
  "current_user": {
    "id": 1,
    "email": "usuario@example.com",
    "name": "João Silva"
  }
}
```

Exemplo com curl (login + acesso protegido):
```bash
# Login para obter token
curl -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{"email":"usuario@example.com","password":"SenhaSegura123!"}'

# Supondo que o token retornado seja <TOKEN>
curl -X GET http://127.0.0.1:5000/protected \
  -H "Authorization: Bearer <TOKEN>"
```

---

## Estrutura de pastas sugerida

A estrutura abaixo é uma sugestão organizada e comum para projetos Flask:

```
.
├── app.py                  # ponto de entrada (ou package app/)
├── config.py               # configurações (produção/desenvolvimento)
├── requirements.txt
├── README.md
├── .env                    # variáveis de ambiente (NÃO commitar)
├── instance/
│   └── app.db              # banco sqlite local
├── app/                    # package da aplicação
│   ├── __init__.py
│   ├── models.py           # modelos/ORM
│   ├── routes.py           # endpoints / blueprints
│   ├── auth.py             # lógica de autenticação (login, jwt callbacks)
│   ├── extensions.py       # instanciação de db, jwt, migrate, etc.
│   └── schemas.py          # validações / marshmallow (opcional)
└── migrations/             # (opcional) arquivos de migração
```

Sinta-se livre para adaptar essa estrutura para suas necessidades (blueprints por domínio, módulos separados para services, repositories, etc).

---

## Boas práticas e notas de segurança

- Use HTTPS em produção para proteger tokens em trânsito.
- Mantenha SECRET_KEY e JWT_SECRET_KEY seguros (não comitar).
- Configure expiração adequada para access tokens e use refresh tokens se necessário.
- Considere implementar blacklist/revocation para logout/token compromise.
- Proteja contra brute force (limitar tentativas de login, rate limiting).
- Armazene senhas usando hashing forte (bcrypt, argon2), nunca em texto plano.
- Valide e sanitize todas as entradas.

---

## Contato

- GitHub: https://github.com/JoaoPedroSilvaDEV2024
- Issues / Pull Requests: Abra uma issue ou PR no repositório do projeto
- E-mail: (adicione seu e-mail aqui, se quiser que usuários possam contatar diretamente)

---

Se quiser, posso:
- Gerar um arquivo de exemplo `app.py` e a estrutura básica do projeto.
- Criar `requirements.txt` com as dependências recomendadas.
- Adicionar exemplos de testes automatizados.
Basta me dizer o que prefere que eu gere em seguida.
