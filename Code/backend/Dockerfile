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

# Install dependencies and copy application files
COPY Code/backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./app ./app

# Expose the port the app will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
