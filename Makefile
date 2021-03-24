SHELL := /bin/bash

export


runtest:
	docker-compose run -e TASK="test" --rm collector

bashapp:
	docker-compose run --rm collector /bin/bash

build:
	docker-compose build collector
