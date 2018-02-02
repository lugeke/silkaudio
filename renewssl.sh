#!/bin/bash

docker run --rm --name letsencrypt \
    -v "/etc/letsencrypt:/etc/letsencrypt" \
    -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
    -v "/data/www/silkaudio:/data/www/silkaudio" \
    certbot/certbot:latest \
    renew --quiet