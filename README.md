# Microservice Boilerplate

A sample microservice project using FastAPI. This project leverages Docker for containerization.


# Project Structure

```bash
#domain(aggregats,events,exception,schemas,comand,queries) unitest
#interface(absractpublisher, abastractrepo, abastractuniofwork(abstractrepo)))
#adapters(kafka et mongodb) test e2e, integration
#sl(unitofwork,)
project_folder/
│
├── src/
│   ├── adapters/
│   │   ├── __init__.py
│   │   └── mongoadapter.py
│   │   └── eventpublisher.py
│   │   └── redisadpter.py
│   │   └── redisRepository.py 
│   ├── entry_point/
│   │   ├── __init__.py
│   │   └── entry_point/
│   │       ├── __init__.py
│   │       └──endpoints.py
│   ├── interfaces/
│   │   ├── __init__.py
│   │   ├── abstractrepository.py
│   │   ├── abstractpublisher.py
│   │   └── abstractUnitOfWork.py
│   │   # Place your interface code here
│   │
│   ├── service_layer/
│   │   ├── __init__.py
│   │   └── handler.py
│   │   └── unity_of_work.py
│   │   └── messageBus.py
│   │
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── events.py
│   │   ├── commands.pyt
│   │   ├── queries.py

│   │   │
│   │   ├── model/
│   │   │   ├── aggregate/
│   │   │   │   ├── __init__.py
│   │   │   │   └── patient.py
│   │   │   │   # Place your aggregate code here
│   │   │   │
│   │   │   ├── entity/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── contact.py
│   │   │   │   ├── communication.py
│   │   │   │   └── link.py
│   │   │   │   # Place your entity code here
│   │   │   │
│   │   │   └── value_object/
│   │   │       ├── __init__.py
│   │   │       └── # Place your value_object code here
│   │   │
│   │   ├── command/
│   │   │   ├── __init__.py
│   │   │   └── # Place your domain command code here
│   │   │
│   │   ├── exception/
│   │   │   ├── __init__.py
│   │   │   └── # Place your domain exception code here
│   │   │
│   │   └── queries/
│   │       ├── __init__.py
│   │       └── # Place your domain queries code here
│   │
│   ├── bootstrap.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── # Place your configuration files here
│   │
│   └── Test/
│       ├── __init__.py
│       └── # Place your tests here
│
├── requirements.txt
├── config.py
└── main.py


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