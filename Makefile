.PHONY: run
run: build
	docker run -itd --name alchemist-timer alchemist-timer /bin/bash

.PHONY: build
build:
	docker build -t alchemist-timer .

.PHONY: stop
stop:
	docker stop alchemist-timer
	docker rm alchemist-timer
	docker rmi alchemist-timer