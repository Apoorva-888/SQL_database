# Dockerized SQL Project
This project demonstrates a simple Dockerized SQL project using Python, SQLite, and Docker.
## Overview
The project includes a Python script (`app.py`) that connects to an SQLite database, creates a table, inserts data, and queries it. The project is Dockerized, allowing easy deployment and execution in a consistent environment.
## Prerequisites
- [Docker](https://www.docker.com/get-started)
    ## Build the Docker image:
    bash
    docker build -t my-sql-app:latest .
   ## Run the Docker container:
    bash
    Copy code
    docker run --name my-sql-container my-sql-app:latest
## Directory Structure
1. app.py: Python script for connecting to SQLite database.
2. Dockerfile: Configuration for building the Docker image.
3. requirements.txt: Empty file as SQLite is part of the Python standard library.
## Notes
The requirements.txt file is intentionally left empty as SQLite is included in the Python standard library.
Customize the Python script (app.py) for your specific use case.
