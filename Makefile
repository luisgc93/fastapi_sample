env-start: ## Start project containers defined in docker-compose
	docker-compose up -d

env-stop: ## Stop project containers defined in docker-compose
	docker-compose stop

env-destroy: ## Destroy all project containers
	docker-compose down -v --rmi local --remove-orphans

clean:  ## Delete all volumes, networks, images & cache
	docker system prune -a --volumes

test: migrate  ## Run tests and generate coverage report
	docker-compose build python_test
	docker-compose run python_test

migrate:  ## Run db migrations
	docker-compose down
	docker-compose build db
	docker-compose build migration
	docker-compose run migration


env-recreate: env-destroy env-start ## Destroy project containers and start them again
