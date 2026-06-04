# 🎓 School API - Cadastro de Alunos, Professores e Turmas

API RESTful desenvolvida com Django e Django REST Framework para gerenciamento de alunos, professores e turmas, com autenticação JWT e documentação Swagger/OpenAPI.

---

## 🚀 Funcionalidades

- Cadastro de Alunos  
- Cadastro de Professores  
- Cadastro de Turmas  
- Relacionamento entre Turmas e Professores  
- Relacionamento entre Turmas e Alunos  
- CRUD completo  
- Autenticação JWT  
- Controle de permissões  
- Documentação Swagger/OpenAPI  
- Validação com Serializers  
- Paginação e filtros  

---

## 🛠 Tecnologias

- Python 3.x  
- Django 4.x  
- Django REST Framework  
- SQLite  
- SimpleJWT  
- drf-spectacular (Swagger)  

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

### Student
```json
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@email.com",
  "birth_date": "2005-03-15"
}
```

### Teacher
```json
{
  "id": 1,
  "name": "Maria Souza",
  "email": "maria@email.com",
  "specialty": "Matemática"
}
```

### Class
```json
{
  "id": 1,
  "name": "Turma A",
  "teacher": 1,
  "students": [1, 2, 3]
}
```

---

## 🔄 Relacionamentos

- Professor (1) → (N) Turmas  
- Turma (N) → (N) Alunos  

---

## 🔐 Autenticação JWT

### Gerar token
POST `/api/token/`

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

### Resposta
```json
{
  "access": "token_de_acesso",
  "refresh": "token_de_refresh"
}
```

---

## 📚 Endpoints

### Students
- GET /api/students/
- POST /api/students/
- GET /api/students/{id}/
- PUT /api/students/{id}/
- DELETE /api/students/{id}/

### Teachers
- GET /api/teachers/
- POST /api/teachers/
- GET /api/teachers/{id}/
- DELETE /api/teachers/{id}/

### Classes
- GET /api/classes/
- POST /api/classes/
- GET /api/classes/{id}/
- PUT /api/classes/{id}/
- DELETE /api/classes/{id}/

---

## 📖 Swagger

Acesse após rodar o projeto:

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

ou

```
http://127.0.0.1:8000/swagger/
```

---

## ⚙️ Instalação

```bash
git clone https://github.com/magnohr/API-de-Cadastro-de-Alunos-Professores-e-Classes.git
cd school-api

python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

---

## 🌐 URLs principais

- Admin → http://127.0.0.1:8000/admin/  
- Token → http://127.0.0.1:8000/api/token/  
- Students → http://127.0.0.1:8000/api/students/  
- Teachers → http://127.0.0.1:8000/api/teachers/  
- Classes → http://127.0.0.1:8000/api/classes/  

---

## 🔐 Como usar JWT (PASSO A PASSO)

1. Gere o token em `/api/token/`  
2. Copie o `access`  
3. Abra o Swagger  
4. Clique em **Authorize**  
5. Cole:

```
Bearer SEU_TOKEN
```

6. Clique em Authorize → Close  
7. Teste os endpoints

---

## ⚠️ Erros comuns

| Problema | Solução |
|----------|--------|
| Bearer duplicado | Use apenas um "Bearer" |
| 401 Unauthorized | Token expirado |
| Swagger não libera | Reautorizar token |
| Token inválido | Gerar novo em `/api/token/` |

---

## 🚀 Fluxo completo

```
/api/token/ → gerar token
→ copiar access
→ Swagger → Authorize
→ testar endpoints
```

---

## 🎯 Aprendizados

- Django REST Framework  
- JWT Authentication  
- Serializers  
- ViewSets  
- Relacionamentos (1-N e N-N)  
- Documentação de API  
- Boas práticas backend  

---

## 👨‍💻 Autor

Magno Henrique Reis  
📧 magnohenriquereis@gmail.com  
🐙 github.com/magnohr
