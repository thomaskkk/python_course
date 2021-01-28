FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade
RUN apk add git bash

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /src
WORKDIR /src

RUN adduser -D user
USER user