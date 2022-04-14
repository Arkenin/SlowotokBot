FROM python:3.8-alpine
LABEL author="Arkenin"

# psycopg2, python dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++

# set work directory
ENV SERVICE=/home/app/service
WORKDIR $SERVICE

# user
RUN addgroup -S app && adduser -S app -G app \
&& mkdir -pv /var/{log,run}/gunicorn/ \
&& chown -cR app:app /var/{log,run}/gunicorn/ 

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .

RUN chown -R app:app $SERVICE
USER app
