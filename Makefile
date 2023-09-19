# Makefile

# Variables
REGISTRY=ghcr.io/fraser-isbester
IMAGE_NAME=metrics
TAG=latest

# Build and tag the Docker image
.PHONY: docker-build
docker-build:
	docker build -t $(REGISTRY)/$(IMAGE_NAME):$(TAG) .
