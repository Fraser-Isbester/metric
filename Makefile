# Makefile

# Variables
REGISTRY=ghcr.io/fraser-isbester
IMAGE_NAME=metrics
TAG=latest

.PHONY: test
test: ## Run's all poetry tests
	python -m pytest -vv

.PHONY: docker-build
docker-build: # Build and tag the Docker image
	docker build -t $(REGISTRY)/$(IMAGE_NAME):$(TAG) .

.PHONY: fix
fix: # Run's a variety of checks and fixes on the codebase
	@autoimport .
	@black .
	@isort .
	@ruff . --fix

.PHONY: clean
clean:
	rm -r .pytest_cache .ruff_cache dist
	rm -r src/**/__pycache__ src/**/.pytest_cache src/**/.ruff_cache
