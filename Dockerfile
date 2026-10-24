FROM node:22.23.4-alpine AS web
# Refresh the system certificate store when rebuilding this image.
RUN apk add --no-cache --upgrade ca-certificates && update-ca-certificates
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM python:3.12-slim AS api
# Refresh the system certificate store when rebuilding this image.
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates \
 && update-ca-certificates \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY api/pyproject.toml api/uv.lock ./
RUN pip install --no-cache-dir uv==0.8.17 && uv sync --locked --no-dev 'certifi>=2026.10.19'
COPY api/main.py ./main.py
EXPOSE 8000
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
