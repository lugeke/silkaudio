#!/bin/bash

cd /home/app/silkaudio && 
git pull origin master && 
docker-compose stop &&
docker-compose run --rm web  python /code/silkaudio/manage.py makemigrations audiobooks &&
docker-compose run --rm web  python /code/silkaudio/manage.py migrate &&
docker-compose build && 
docker-compose up -d