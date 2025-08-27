FROM python:3.12-slim as builder

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/poetry /usr/local/bin/poetry
COPY --from=builder /app /app

CMD ["poetry", "run", "python", "-m", "bot"]