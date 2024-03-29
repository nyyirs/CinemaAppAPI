FROM python:3.7.6-alpine3.10
LABEL Key = "Nyyir"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D nyyir
USER nyyir
