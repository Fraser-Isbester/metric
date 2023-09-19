# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy only pyproject.toml to install dependencies
COPY pyproject.toml /app/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copy the current directory contents into the container at /app
COPY src/ /app/

# Run your application
CMD ["python", "main.py"]
