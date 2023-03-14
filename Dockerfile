# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
COPY config.example.ini config.ini

#ARG INTERFACE="websocket"

CMD [ "python3", "main.py" , "$INTERFACE"]