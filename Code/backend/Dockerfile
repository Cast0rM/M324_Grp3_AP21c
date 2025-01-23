# syntax = docker/dockerfile:1.4

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /app

# Build arguments for database configurations
ARG ALBUM_USERNAME
ARG ALBUM_PASSWORD
ARG ALBUM_HOST
ARG ALBUM_PORT
ARG ALBUM_DATABASE
ARG BANDS_USERNAME
ARG BANDS_PASSWORD
ARG BANDS_HOST
ARG BANDS_PORT
ARG BANDS_DATABASE

# Set environment variables from build arguments
ENV ALBUM_USERNAME=$ALBUM_USERNAME \
    ALBUM_PASSWORD=$ALBUM_PASSWORD \
    ALBUM_HOST=$ALBUM_HOST \
    ALBUM_PORT=$ALBUM_PORT \
    ALBUM_DATABASE=$ALBUM_DATABASE \
    BANDS_USERNAME=$BANDS_USERNAME \
    BANDS_PASSWORD=$BANDS_PASSWORD \
    BANDS_HOST=$BANDS_HOST \
    BANDS_PORT=$BANDS_PORT \
    BANDS_DATABASE=$BANDS_DATABASE

# Copy requirements and install dependencies
COPY requirements.txt ./ 
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Copy application code
COPY ./app ./app

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Start FastAPI application with Gunicorn, binding to 0.0.0.0:8000
CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:8000", "--workers", "2"]
