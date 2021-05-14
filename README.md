# DjangoForPros

This is a bookstore website which uses Python/Django and is deployed on Heroku at https://andys-bookstore.herokuapp.com/

To run locally, clone the repository (Clone to WSL if using Windows) and :-

Install Docker
run command: docker-compose up -d --build
run command: docker-compose exec web python manage.py migrate

Books can be added via the Django Admin Panel

Main Page : localhost:8000
Django Admin : localhost:8000/admin-for-django

In order for the website to work, a valid SENDGRID_API_KEY needs to be set locally in docker-compose.yml or config/.env

