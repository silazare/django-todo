#!/bin/sh
pipenv run python manage.py migrate
pipenv run python manage.py hopper || true
pipenv run python manage.py runserver 0.0.0.0:8000
