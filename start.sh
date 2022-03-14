#!/bin/sh
python3 /code/manage.py migrate
exec "$@"