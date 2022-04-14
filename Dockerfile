FROM python:3.8-slim
LABEL author="Arkenin"

ENV SERVICE=/home/app/service
RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER

RUN mkdir -p $SERVICE
RUN mkdir -p $SERVICE/static

# install psycopg2 dependencies
RUN apt-get update && \
    apt-get -y install libpq-dev gcc && \
    apt-get install -y locales locales-all && \
    locale-gen pl_PL.UTF-8

# Python stuff
RUN pip install --upgrade pip
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt


RUN mkdir -p /code
COPY *.py /code/
WORKDIR /code

CMD python main.py

FROM python:3.8.3-alpine

ENV MICRO_SERVICE=/home/app/microservice
RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER
# set work directory




# where the code lives
WORKDIR $MICRO_SERVICE

# set environment variables

# install psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++
# install dependencies
RUN pip install --upgrade pip
# copy project
COPY . $MICRO_SERVICE
RUN pip install -r requirements.txt
COPY ./entrypoint.sh $MICRO_SERVICE

CMD ["/bin/bash", "/home/app/microservice/entrypoint.sh"]