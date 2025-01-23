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

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY ./app ./app

FROM builder as dev-envs

# Ensure non-interactive mode for apt
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add development user
RUN useradd -s /bin/bash -m vscode && \
    groupadd docker && \
    usermod -aG docker vscode

# Install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /