# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the necessary files to install dependencies
COPY pyproject.toml /app/

# Configure Poetry:
# - Do not create a virtual environment inside the container
# - Install only package dependencies; skip dev dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

# Copy the rest of the application
COPY . .

# Command to run the application
CMD ["python", "main.py"]
