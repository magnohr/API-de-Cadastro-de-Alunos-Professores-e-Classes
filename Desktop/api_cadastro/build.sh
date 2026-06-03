#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python school_api/manage.py collectstatic --no-input
python school_api/manage.py migrate
