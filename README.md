# 🎓 School API - Cadastro de Alunos, Professores e Turmas

API RESTful desenvolvida com Django e Django REST Framework para gerenciamento de alunos, professores e turmas, utilizando autenticação JWT, documentação Swagger/OpenAPI e operações completas de CRUD.

---

## 🚀 Funcionalidades

- ✅ Cadastro de Alunos  
- ✅ Cadastro de Professores  
- ✅ Cadastro de Turmas  
- ✅ Relacionamento entre Turmas e Professores  
- ✅ Relacionamento entre Turmas e Alunos  
- ✅ CRUD completo  
- ✅ Autenticação JWT  
- ✅ Controle de permissões  
- ✅ Documentação Swagger/OpenAPI  
- ✅ Validação com Serializers  
- ✅ Paginação e filtros  

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
🗄 Modelagem
Student
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@email.com",
  "birth_date": "2005-03-15"
}
Teacher
{
  "id": 1,
  "name": "Maria Souza",
  "email": "maria@email.com",
  "specialty": "Matemática"
}
Class
{
  "id": 1,
  "name": "Turma A",
  "teacher": 1,
  "students": [1, 2, 3]
}
🔄 Relacionamentos
Professor (1) → (N) Turmas
Turma (N) → (N) Alunos
🔐 Autenticação JWT
Gerar token
POST /api/token/
Exemplo de requisição
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
Resposta
{
  "access": "token_de_acesso",
  "refresh": "token_de_refresh"
}
📚 Endpoints
Students
GET /api/students/
POST /api/students/
GET /api/students/{id}/
PUT /api/students/{id}/
DELETE /api/students/{id}/
Teachers
GET /api/teachers/
POST /api/teachers/
GET /api/teachers/{id}/
DELETE /api/teachers/{id}/
Classes
GET /api/classes/
POST /api/classes/
GET /api/classes/{id}/
PUT /api/classes/{id}/
DELETE /api/classes/{id}/
📖 Documentação Swagger

Após rodar o projeto:

python manage.py runserver

Acesse:

http://127.0.0.1:8000/api/schema/swagger-ui/

ou:

http://127.0.0.1:8000/swagger/
⚙️ Instalação
1. Clone o repositório
git clone https://github.com/magnohr/API-de-Cadastro-de-Alunos-Professores-e-Classes.git
cd school-api
2. Crie ambiente virtual
python -m venv .venv
3. Ative o ambiente

Windows

.venv\Scripts\activate

Linux/Mac

source .venv/bin/activate
4. Instale dependências
pip install -r requirements.txt
5. Execute migrations
python manage.py makemigrations
python manage.py migrate
6. Crie usuário admin
python manage.py createsuperuser
7. Rode o servidor
python manage.py runserver
🌐 URLs principais
Admin → http://127.0.0.1:8000/admin/
Token → http://127.0.0.1:8000/api/token/
Students → http://127.0.0.1:8000/api/students/
Teachers → http://127.0.0.1:8000/api/teachers/
Classes → http://127.0.0.1:8000/api/classes/
🔐 Como usar JWT (PASSO A PASSO)
1. Gere o token

Faça POST em:

/api/token/
2. Copie o access token
3. No Swagger clique em Authorize

Cole no formato:

Bearer SEU_TOKEN
4. Teste os endpoints normalmente
📸 Demonstração
Swagger UI funcionando
Django Admin
CRUD completo
Autenticação JWT
🎯 Aprendizados
Django REST Framework
JWT Authentication
Serializers
ViewSets
Relacionamentos (1-N e N-N)
Documentação de API
Boas práticas backend
👨‍💻 Autor

Magno Henrique Reis
📧 magnohenriquereis@gmail.com
🐙 GitHub: https://github.com/magnohr
