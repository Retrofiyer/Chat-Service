# Stage 1: Build
FROM python:3.12.5-slim AS build

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Final Stage
FROM python:3.12.5-slim


WORKDIR /app

COPY --from=build /app /app

CMD ["python", "run.py"]