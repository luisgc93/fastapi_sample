start: ## Start project containers defined in docker-compose
	docker-compose up -d

create-migration: start ## Autogenerate an alembic migration
	docker-compose run backend alembic revision --autogenerate -m "$(migration-name)"

migrate: recreate start ## Apply the latest migrations
	docker-compose run backend alembic upgrade head

psql: start  ##  Connect to the db
	docker-compose run db psql -h db -d test_db -U postgres

stop: ## Stop project containers defined in docker-compose
	docker-compose stop

destroy: ## Destroy all project containers
	docker-compose down -v --rmi local --remove-orphans

clean:  ## Delete all volumes, networks, images & cache
	docker system prune -a --volumes

test: recreate ## Run tests and generate coverage report
	docker-compose build python_test
	docker-compose run python_test

recreate: destroy start ## Destroy project containers and start them again
