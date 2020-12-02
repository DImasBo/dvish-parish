#! /usr/bin/env bash
set -e
set -x

python manage.py migrate
pytest --cov=app --cov-report=xml "${@}"
