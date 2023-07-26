FROM python:3.10-rc-slim-bullseye

# Install poetry for dependencies management
RUN pip install poetry

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying requirements of a project
COPY pyproject.toml poetry.lock /app/

# Set working directory
WORKDIR /app

# Installing requirements
RUN poetry install

# Copying actual application
COPY ./src /app/src
# Copying actual test files
COPY ./tests /app/tests

# Launch Microservice
CMD ["poetry", "run", "python", "-m", "src"]
