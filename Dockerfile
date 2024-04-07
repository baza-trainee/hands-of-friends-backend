FROM python:3.10.7-slim-buster
LABEL maintainer="olena.liuby@gmail.com"

ENV PORT=8000 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libffi-dev \
    libcairo2 \
    gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
