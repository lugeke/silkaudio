#!/bin/bash

cd /home/app/silkaudio && 
git pull origin master && 
docker-compose stop &&
docker-compose run --rm web  python /code/silkaudio/manage.py makemigrations audiobooks &&
docker-compose run --rm web  python /code/silkaudio/manage.py migrate &&
docker-compose build --build-arg APP_ENV=dev && 
docker-compose -f docker-compose.yml -f production.yml up -d