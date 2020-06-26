FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp-build-deps \
       gcc libc-dev linux-headers
RUN apk add git tree sqlite
RUN pip install -r /requirements.txt
RUN pip install git+https://github.com/zalando/connexion.git connexion[swagger-ui]
RUN apk del .tmp-build-deps

RUN mkdir /framework
WORKDIR /framework
COPY ./framework /framework