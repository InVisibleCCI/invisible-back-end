#!/bin/sh
python3 /code/manage.py migrate
python3 /code/manage.py crontab add
exec "$@"