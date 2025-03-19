OPS_DIR=./ops

start: prepare 

	cd $(OPS_DIR) && docker-compose up -d --force-recreate --build

prepare:

	cp pyproject.toml $(OPS_DIR)/

logs:

	docker compose logs -f

api-logs:

	docker compose logs -f 
