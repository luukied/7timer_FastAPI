FROM python:3.9-alpine AS api

WORKDIR /code

COPY requirements.txt ./
COPY app ./app

RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt 

CMD . /opt/venv/bin/activate \
    && python app/main.py