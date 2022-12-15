docker-compose up:
	docker-compose -f docker-compose.yml up -d

deps:
	pip install Flake8-pyproject black isort pytest

lint: deps
	flake8 .
	black .
	isort .
