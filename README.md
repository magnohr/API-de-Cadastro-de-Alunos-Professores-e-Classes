# 🎓 School API - Cadastro de Alunos, Professores e Turmas

API RESTful desenvolvida com Django e Django REST Framework para gerenciamento de alunos, professores e turmas, utilizando autenticação JWT, documentação Swagger/OpenAPI e operações completas de CRUD.

## 🚀 Funcionalidades

- ✅ Cadastro de Alunos
- ✅ Cadastro de Professores
- ✅ Cadastro de Turmas
- ✅ Relacionamento entre Turmas e Professores
- ✅ Relacionamento entre Turmas e Alunos
- ✅ CRUD Completo
- ✅ Autenticação JWT
- ✅ Controle de Permissões
- ✅ Documentação Swagger/OpenAPI
- ✅ Validação de Dados com Serializers
- ✅ Paginação e Filtros

---

## 🛠 Tecnologias Utilizadas

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite
- SimpleJWT
- drf-spectacular
- Swagger UI

---

## 📂 Estrutura do Projeto

```bash
school_api/
│
├── students/
├── teachers/
├── classes/
├── school_api/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🗄 Modelagem

### 👨‍🎓 Student

```json
{
    "id": 1,
    "name": "João Silva",
    "email": "joao@email.com",
    "birth_date": "2005-03-15"
}
```

### 👨‍🏫 Teacher

```json
{
    "id": 1,
    "name": "Maria Souza",
    "email": "maria@email.com",
    "specialty": "Matemática"
}
```

### 🏫 Class

```json
{
    "id": 1,
    "name": "Turma A",
    "teacher": 1,
    "students": [1,2,3]
}
```

---

## 🔄 Relacionamentos

```text
Professor (1) -------- (N) Turmas

Turma (N) -------- (N) Alunos
```

---

## 🔐 Autenticação JWT

### Gerar Token

```http
POST /api/token/
```

Exemplo:

```json
{
    "username": "admin",
    "password": "123456"
}
```

Resposta:

```json
{
    "access": "token...",
    "refresh": "token..."
}
```

### Atualizar Token

```http
POST /api/token/refresh/
```

---

## 📚 Endpoints

### 👨‍🎓 Students

| Método | Endpoint |
|----------|----------|
| POST | /api/students/ |
| GET | /api/students/ |
| GET | /api/students/{id}/ |
| PUT | /api/students/{id}/ |
| DELETE | /api/students/{id}/ |

### 👨‍🏫 Teachers

| Método | Endpoint |
|----------|----------|
| POST | /api/teachers/ |
| GET | /api/teachers/ |
| GET | /api/teachers/{id}/ |
| PUT | /api/teachers/{id}/ |
| DELETE | /api/teachers/{id}/ |

### 🏫 Classes

| Método | Endpoint |
|----------|----------|
| POST | /api/classes/ |
| GET | /api/classes/ |
| GET | /api/classes/{id}/ |
| PUT | /api/classes/{id}/ |
| DELETE | /api/classes/{id}/ |

---

## 📖 Documentação Swagger

Após iniciar o projeto:

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/api/schema/swagger-ui/
```

ou

```text
http://127.0.0.1:8000/swagger/
```

(dependendo da configuração adotada)

---

## ⚙️ Instalação

Clone o projeto:

```bash
[git clone https://github.com/seuusuario/school-api.git
](https://github.com/magnohr/API-de-Cadastro-de-Alunos-Professores-e-Classes.git)```

Entre na pasta:

```bash
cd school-api
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

Crie um superusuário:

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
```

---

## 📸 Demonstração

Adicione aqui imagens ou GIFs mostrando:

- Swagger UI funcionando
- <img width="1340" height="595" alt="image" src="https://github.com/user-attachments/assets/58d6569e-6f94-4185-9572-ff7c6cae9ef8" />


- Django Admin
- <img width="921" height="528" alt="image" src="https://github.com/user-attachments/assets/f0257e88-d2fe-4e9e-91c0-03e4c23c844e" />

- Testes no Postman
- Autenticação JWT
- <img width="1216" height="543" alt="image" src="https://github.com/user-attachments/assets/1f1f67da-4b97-4c90-a32d-734cc131545b" />

- CRUD de Alunos
- CRUD de Professores
- CRUD de Turmas

---

## 🎯 Aprendizados

Este projeto foi desenvolvido para praticar:

- Django REST Framework
- Arquitetura REST
- JWT Authentication
- Relacionamentos entre Models
- Serializers
- ViewSets
- Permissions
- Documentação de APIs
- Boas práticas de desenvolvimento backend

---
caminhos:

 http://127.0.0.1:8000/admin/


http://127.0.0.1:8000/api/token/


GET (Listar): http://127.0.0.1:8000/api/students/
POST (Criar): http://127.0.0.1:8000/api/students/

GET (Listar): http://127.0.0.1:8000/api/teachers/
POST (Criar): http://127.0.0.1:8000/api/teachers/


GET (Listar): http://127.0.0.1:8000/api/classes/
POST (Criar): http://127.0.0.1:8000/api/classes/

## 👨‍💻 Autor

**Magno Henrique reis**

📧 magnohenriquereis@gmail.com 
💼 [LinkedIn](https://www.linkedin.com/feed/?shareActive=true&shareUrl=https%3A%2F%2Fdio.me%2Fcertificate%2FZKTQRBNF&linkOrigin=LI_BADGE)  
🐙 [GitHub](https://github.com/magnohr/magnohr)

---

⭐ Se este projeto foi útil para você, deixe uma estrela no repositório.
