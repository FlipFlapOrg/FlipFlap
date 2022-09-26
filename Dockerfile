FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add  --no-cache build-base mariadb-dev

RUN mkdir -p /app
WORKDIR /app

ENV PYTHONPATH "/app:$PYTHONPATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "main:app"]