FROM python:3.12-slim

RUN pip install poetry django uvicorn psycopg2-binary

COPY pyproject.toml poetry.lock

COPY . .

RUN poetry install -n

EXPOSE 8000

ENTRYPOINT [ "poetry","run"]

CMD ["uvicorn","SaaS.asgi:application","--host","0.0.0.0","--port","8000"]