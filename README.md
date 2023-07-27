# Microservice Boilerplate

A sample microservice project using FastAPI. This project leverages Docker for containerization.


# Project Structure

```bash
#domain(aggregats,events,exception,schemas,comand,queries) unitest
#interface(absractpublisher, abastractrepo, abastractuniofwork(abstractrepo)))
#adapters(kafka et mongodb) test e2e, integration
#sl(unitofwork,)
#tester en cas d'echec et de reussite
Microservice
│
├── src
│   └── app
│   │   ├── application.py  # FastAPI application
│   │   ├── lifetime.py     # Startup/Shutdown handlers
│   │   ├── router.py       # Main router
│   |   ├── monitoring      # Monitoring service
│   |   |   ├── schema.py   # Response models
│   |   |   └── router.py   # Router
│   ├── config.py           # Application settings
│   ├── logging.py          # Logging formatters
│   ├── __init__.py         # Application version
│   ├── __main__.py         # Startup script for uvicorn
├── tests                   # Tests for project
|   ├── conftest.py         # Tests configuration / fixtures
|   ├── monitoring          # Tests for the monitoring service
|   |   └── test_health.py  # Tests for the Health check route
├── .pre-commit-config.yaml # Pre-commit configuration
├── Dockerfile              # Docker file
├── docker-compose.yaml     # Docker Compose file
├── Makefile
├── LICENSE.txt
├── poetry.lock
├── pyproject.toml          # Project Definition
└── README.md

```

## Dependencies

This project uses poetry, a modern dependency management tool.

To run the project use this set of commands:

```bash
poetry install
poetry run start
```

This will start the server on the configured host.

You can find Swagger documentation at `/docs`.

You can find Redoc documentation at `/redoc`.

You can read more about poetry here: https://python-poetry.org/


# Running with docker

To run the service, simply run the following command :

```bash
docker-compose up
```

# Running locally

To run the service, simply run the following command :

```bash
docker-compose up
```

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possibe bugs);
* yesqa (removes useless `# noqa` comments).


You can read more about pre-commit here: https://pre-commit.com/


# Running Tests

All tests are located under the <i>tests</i> folder. To run them from terminal, execute the following command :

```bash
poetry run pytest -v tests
```

To run tests with coverage, run the following command :

```bash
poetry run coverage run -m pytest -v && poetry run coverage report -m
```