build:
	docker-compose up --build -d

beautiful:
	docker-compose exec django_app python manage.py collectstatic

migrate:
	docker-compose exec django_app python manage.py makemigrations
	docker-compose exec django_app python manage.py migrate

superuser:
	docker-compose exec -it django_app python manage.py createsuperuser

stop:
	docker-compose down

kill:
	docker system prune -a -f