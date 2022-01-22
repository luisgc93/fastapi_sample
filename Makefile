start: ## Start project containers defined in docker-compose
	docker-compose up -d

stop: ## Stop project containers defined in docker-compose
	docker-compose stop

destroy: ## Destroy all project containers
	docker-compose down -v --rmi local --remove-orphans

clean:  ## Delete all volumes, networks, images & cache
	docker system prune -a --volumes

test: start ## Run tests and generate coverage report
	docker-compose build python_test
	docker-compose run python_test


env-recreate: env-destroy env-start ## Destroy project containers and start them again
