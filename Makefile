.PHONY: run
run: build
	docker compose up -d

.PHONY: build
build:
	docker build -t alchemist_timer .

.PHONY: stop
stop:
	docker compose down