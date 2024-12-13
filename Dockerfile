FROM python:3.12

WORKDIR /code

COPY . .

RUN pip install --quiet poetry

RUN poetry config virtualenvs.create false

RUN poetry install --only=main --no-cache
