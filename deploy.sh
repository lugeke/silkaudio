#!/bin/bash



ssh do 'cd /home/app/silkaudio && git pull origin master && docker-compose up -d'  