#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python school_api/manage.py collectstatic --no-input
python school_api/manage.py migrate

# Cria o superusuario automaticamente se ele nao existir no banco de dados da nuvem
python school_api/manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None"
