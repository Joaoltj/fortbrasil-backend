FROM python:3.6-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN python -m venv venv
RUN . venv/bin/activate

ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DATABASE_URL='postgresql://postgres:postgres@192.168.1.103:5432/fortbrasil'

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


EXPOSE 5000

COPY . .
CMD flask db upgrade

