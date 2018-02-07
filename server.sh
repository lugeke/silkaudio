#!/bin/bash

cd /home/app/silkaudio && 
git pull origin master && 
docker-compose stop &&

docker-compose build --build-arg APP_ENV=prod nginx  && 
docker-compose build --build-arg APP_ENV=prod web  && 
docker-compose build postgres &&
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d