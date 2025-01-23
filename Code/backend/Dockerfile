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

# Install dependencies
COPY requirements.txt ./ 
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Copy application code to the container
COPY ./app ./app

# Default command to run when the container starts
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "main:app"]

