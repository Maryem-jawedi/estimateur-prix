ENV = --env-file .env -f infra/docker-compose.yml

up:
	docker compose $(ENV) up -d --build

down:
	docker compose $(ENV) down

logs:
	docker compose $(ENV) logs -f

test:
	pytest -q

lint:
	ruff check
