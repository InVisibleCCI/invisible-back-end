FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN         apt-get update && apt-get install -y gcc libmariadb-dev

RUN         mkdir /code && mkdir /poetry
ADD         ./poetry/pyproject.toml    /pyproject.toml
ADD         ./poetry/poetry.lock       /poetry.lock

WORKDIR     /poetry
RUN         pip install --upgrade pip \
            && pip install poetry \
            && poetry config virtualenvs.create false \
            && poetry install --no-interaction


#ADD         ./start.sh          /start.sh
#RUN         chmod +x            /start.sh

WORKDIR     /code
ADD         ./src .

EXPOSE      8000

#CMD         gunicorn sferenobackend.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 300