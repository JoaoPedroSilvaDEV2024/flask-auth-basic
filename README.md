# Flask User Auth API 🔐

Uma API RESTful minimalista para autenticação de usuários, demonstrando o uso de persistência em banco de dados SQL e segurança com tokens JWT.

## 🚀 Tecnologias
* **Python 3**
* **Flask**: Micro-framework web.
* **SQLite**: Banco de dados relacional embutido.
* **PyJWT**: Geração e validação de tokens JSON Web Token.
* **Werkzeug**: Hash e verificação de senhas.

## 📁 Estrutura do Projeto
* `app.py`: Servidor principal e definição das rotas (Register, Login, Protected).
* `database.py`: Configuração do banco de dados e criação automática da tabela de usuários.
* `requirements.txt`: Lista de dependências do projeto.

## ⚙️ Configuração e Instalação

1. **Criar Ambiente Virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

2. **Instalar Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar a API:**
   ```bash
   python app.py
   ```

## 📍 Endpoints

### 1. Registro (`POST /register`)
Cria um novo usuário.
* **Payload:** `{"username": "admin", "password": "123"}`

### 2. Login (`POST /login`)
Gera um token JWT válido por 2 horas.
* **Payload:** `{"username": "admin", "password": "123"}`
* **Retorno:** `{"token": "string_do_token"}`

### 3. Área Protegida (`GET /protected`)
Valida se o usuário está autenticado.
* **Header Requerido:** `Authorization: <SEU_TOKEN>`

## ⚠️ Observações de Segurança
- A `SECRET_KEY` está hardcoded para fins de exemplo; em produção, deve ser lida de uma variável de ambiente.
- O banco `users.db` é criado automaticamente na primeira execução.

