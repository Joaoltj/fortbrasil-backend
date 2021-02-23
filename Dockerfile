FROM python:3.9-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev
RUN apk add --update musl-dev gcc libffi-dev

RUN pip install --upgrade pip

RUN python -m venv venv
RUN . venv/bin/activate

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
ENV DATABASE_URL='postgresql://fortbrasil:fortbrasil@db:5432/fortbrasil'

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


EXPOSE 5000

COPY . .


CMD ["flask", "run"]

