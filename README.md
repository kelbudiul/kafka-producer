# Kafka Producer for Synthetic Data Streaming

## Overview

This project is a configurable Kafka producer application designed to generate and stream synthetic data to a Kafka topic. It's ideal for simulating real-time data streams, testing Kafka-based applications, and developing data pipelines.

## Features

- **Flexible Data Generation**: Uses a configurable schema to create various types of synthetic data.
- **Multiple Operating Modes**: Supports both single message and batch message sending.
- **Customizable Configuration**: Easy to configure Kafka settings, data generation parameters, and runtime behavior.
- **Docker Support**: Includes Dockerfile for easy containerization and deployment.
- **Scalable Architecture**: Built with modularity in mind for easy extension and modification.

## Prerequisites

- Python 3.11+
- Poetry (for dependency management)
- Access to a Kafka broker

## Installation

1. Clone the repository:
   ```
   git clone [repository-url]
   cd kafka-producer
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Configuration

1. Kafka and Application Settings:
   - Edit `config.toml` to set Kafka broker details, topic name, and operational mode.

2. Data Generation Schema:
   - Modify `schema.toml` to define the structure of the synthetic data you want to generate.

## Usage

1. Run the application:
   ```
   poetry run python main.py
   ```

2. To run in Docker:
   ```
   docker build -t kafka-producer .
   docker run kafka-producer
   ```

## Project Structure

- `main.py`: Entry point of the application.
- `generator.py`: Contains the `DataGenerator` class for creating synthetic data.
- `producer.py`: Implements the Kafka `Producer` class for sending messages.
- `config.toml`: Configuration file for Kafka and application settings.
- `schema.toml`: Defines the schema for synthetic data generation.
- `utils.py`: Utility functions, including configuration loading.
- `Dockerfile`: Instructions for containerizing the application.

## Customization

- To add new data types, extend the `DataGenerator` class in `generator.py`.
- For different message formats or Kafka configurations, modify the `Producer` class in `producer.py`.
- Adjust the main loop in `main.py` to change the overall behavior of the application.
