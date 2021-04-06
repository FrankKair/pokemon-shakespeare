# syntax = docker/dockerfile:1.0-experimental
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app
COPY ./requirements.txt ./
COPY ./main.py ./
COPY ./src ./src
RUN pip install -r requirements.txt
