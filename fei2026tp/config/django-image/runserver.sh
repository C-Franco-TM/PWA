#!/bin/bash
set -e

cd /usr/src/app

if [ ! -f manage.py ]; then
    django-admin startproject config .
fi

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput || true
python manage.py runserver 0.0.0.0:8000
