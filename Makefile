include .env

default: install test lint

test: lint test.all

test.cov: test.coverage

test.all:
	@pytest tests

test.coverage:
	@coverage run -m pytest -vv tests && coverage report -m --omit="*/test*,config/*.conf" --fail-under=85

install:
	@poetry install

lint:
	@pylint src tests

format.check:
	@black . --check

format.fix:
	@black .

image.build:
	./build-image.sh

run.container:
	@docker run -d --name bookapi -p 8000:8000 bookapi

stop.container:
	@docker stop bookapi && docker rm bookapi
