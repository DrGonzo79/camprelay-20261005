FROM node:22-alpine AS web
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM python:3.12-slim AS api
WORKDIR /app
COPY api/pyproject.toml api/uv.lock ./
RUN pip install --no-cache-dir uv==0.8.17 && uv sync --locked --no-dev
COPY api/main.py ./main.py
EXPOSE 8000
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
