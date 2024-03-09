FROM python:3.10.7-slim-buster
LABEL maintainer="olena.liuby@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get -y install libpq-dev gcc gettext && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py compilemessages

RUN python manage.py collectstatic --noinput

RUN mkdir -p /vol/web/media

RUN adduser --disabled-password --no-create-home django-user && \
    chown -R django-user:django-user /vol/ && \
    chmod -R 755 /vol/web/

USER django-user
