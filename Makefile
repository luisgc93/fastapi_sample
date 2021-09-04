PROJECT_ROOT_FOLDER := $(shell pwd)
DOCKER_COMPOSE_FILE := $(PROJECT_ROOT_FOLDER)/docker-compose.yml

env-start: ## Start project containers defined in docker-compose
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d

env-stop: ## Stop project containers defined in docker-compose
	docker-compose -f $(DOCKER_COMPOSE_FILE) stop

env-destroy: ## Destroy all project containers
	docker-compose -f $(DOCKER_COMPOSE_FILE) down -v --rmi local --remove-orphans


env-recreate: env-destroy env-start ## Destroy project containers and start them again