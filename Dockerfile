# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /app

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
COPY config.example.ini config.ini

ENV INTERFACE="websocket"

CMD [ "sh", "-c", "python3 main.py $INTERFACE"]