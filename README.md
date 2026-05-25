# Core Banking System API

API bancária desenvolvida com Python e Flask utilizando **Arquitetura em Camadas (Layered Architecture)**, autenticação JWT e regras de negócio estruturadas.

Deploy: [Acesse a API no Render](https://sistema-bancario-layered-architecture.onrender.com/)

---

## Tecnologias & Conceitos

### Stack Tecnológica
- Backend: Python, Flask, SQLAlchemy
- Banco de Dados: PostgreSQL
- Segurança: JWT (JSON Web Tokens), Bcrypt (Hash de senhas)
- Testes & Deploy: Pytest, Render

### Conceitos Aplicados
- Arquitetura em Camadas (Separation of Concerns)
- Design de API RESTful & Programação Orientada a Objetos (POO)
- Middlewares de Autenticação & Validação de CPF
- Tratamento de Regras de Negócio Bancárias (Saque, Depósito, Transferência)

---

## Arquitetura dos Endpoints

As rotas protegidas utilizam token JWT via Header:
Authorization: Bearer seu_token

| Método | Endpoint | Descrição | Requer JWT |
| :--- | :--- | :--- | :---: |
| POST | /cadastro | Cria um novo cliente no sistema | No |
| POST | /login | Autentica o usuário e retorna o token | No |
| POST | /depositar | Realiza um depósito em uma conta | Yes |
| POST | /sacar | Realiza um saque validando o saldo | Yes |
| POST | /transferir | Transfere valores entre duas contas | Yes |
| GET | /buscar_cliente/<id> | Retorna os dados do cliente | Yes |
| GET | /buscar_conta/<id> | Retorna os dados da conta | Yes |
| GET | /ver_saldo/<id> | Retorna o saldo atualizado | Yes |

---

## Exemplos de Requisição (Payloads) e Respostas

### Cadastro (POST /cadastro)

    {
      "nome": "Pedro",
      "cpf": "00000000000",
      "senha": "123456"
    }

### Login (POST /login)

    {
      "cpf": "00000000000",
      "senha": "123456"
    }

*Resposta esperada do Login:*

    {
      "token": "jwt_token"
    }

### Depositar (POST /depositar)

    {
      "id_conta": 1,
      "valor": 100
    }

### Sacar (POST /sacar)

    {
      "id_conta": 1,
      "valor": 50
    }

### Transferir (POST /transferir)

    {
      "conta_origem": 1,
      "conta_destino": 2,
      "valor": 100
    }

---

## Como Executar o Projeto Localmente

1. Clone o repositório:
    git clone https://github.com/pedro751ok-svg/sistema_bancario_layered-architecture.git
    cd sistema_bancario_layered-architecture

2. Configure o ambiente virtual:
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate

3. Instale as dependências:
    pip install -r requirements.txt

4. Execute a aplicação:
    flask run

---

## Autor

**Pedro Henrique Messias Neris**
- GitHub: [@pedro751ok-svg](https://github.com/pedro751ok-svg)
- LinkedIn: [meu perfil do linkedin](https://www.linkedin.com/in/pedro-mesias-727715264)
