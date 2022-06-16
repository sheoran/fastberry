FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /app
RUN pip install poetry==1.1.13
COPY ./app/pyproject.toml ./app/poetry.lock* /app/

# Add in future if required to further optimize image --no-dev
RUN poetry install --no-interaction --no-ansi --no-root
COPY ./app /app
ENV PYTHONPATH=/app
