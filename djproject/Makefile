start:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations $(app)

createsuperuser:
	poetry run python manage.py createsuperuser

new-app:
	poetry run python manage.py startapp $(app)
	@# to execute run `make new-app app=cenas`

py3clean:
	py3clean .

compose.setup:
	@$(MAKE) compose.start

compose.start:
	docker compose up --build --force-recreate

compose.migrate: compose.migrations
	docker compose run --rm web poetry run python manage.py migrate

compose.migrations:
	docker compose run --rm web poetry run python manage.py makemigrations

compose.collectstatic:
	docker compose exec web poetry run python manage.py collectstatic --noinput

compose.createsuperuser:
	docker compose run --rm web poetry run python manage.py createsuperuser