-include .env
export

dev.install:
	@poetry install

lint:
	@mypy service
	@flake8 service

run:
	@python -m service

debug.run:
	@adev runserver service/main.py