# Django Template 2.0

Develop a Django template that could handle concurrent request, CI/CD integrations,
discover better deployment platform, docker, explore ECS and so on

# Getting Started

### Dependencies

* Docker
* Python3

### For Local Development
```
docker-compose up
```
### To rebuild image specially if there is changes on requirements.txt
```
docker-compose up --build
```
### To run migrations inside docker container
```
docker exec -it django-project_django_1  python manage.py makemigrations
docker exec -it django-project_django_1  python manage.py migrate
```

# Testing

### To run the unit tests using coverage:
```
coverage run manage.py test
```

### To add verbosity (level 2 is recommended):
```
coverage run manage.py test -v 2 --no-logs
docker exec -it django-project_django_1 coverage run manage.py test -v 2 --no-logs
```

### To run specific test case
```
coverage run manage.py test domain.users.tests -v 2
```

### To generate the coverage report:
```
coverage html

or

coverage report
```

### Combine All tests commands
```
docker exec -it django-project_django_1 coverage run manage.py test -v 2 --no-logs
docker exec -it django-project_django_1 coverage html
open htmlcov/index.html
```
### Run Locust (Load Testing)
```
locust --host=http://localhost:8000
```

# Django Commands

### Create Super User
```
docker exec -it django-project_django_1 python manage.py createsuperuser
```

### Clean all the data from the database, but will not delete the tables
```
docker exec -it django-project_django_1 python manage.py flush
```

### Django deployment checklist
```
docker exec -it django-project_django_1 python manage.py check --deploy
```

### Seeders

This command will create:

20 users and their corresponding profiles
10 stores for each user (a total of 200 stores)
15 categories
8 products for each store (a total of 1600 products)

```
docker exec -it django-project_django_1 python manage.py reset_data
docker exec -it django-project_django_1 python manage.py data_seeder --users 20 --stores 10 --categories 15 --products 8
```


### TODO:

- Django Data Seeder and Improve local Development
