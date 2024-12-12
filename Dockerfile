FROM python:3.12

WORKDIR /code

COPY . .

RUN pip install --quiet poetry

RUN poetry install --only=main --no-cache

ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]