env-start: ## Start project containers defined in docker-compose
	docker-compose up -d

env-stop: ## Stop project containers defined in docker-compose
	docker-compose stop

env-destroy: ## Destroy all project containers
	docker-compose down -v --rmi local --remove-orphans

clean:  ## Delete all images
	docker rmi -f $(docker images -a -q)

test:
	docker-compose run python_test

env-recreate: env-destroy env-start ## Destroy project containers and start them again