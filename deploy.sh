#!/bin/bash

host=root@138.68.178.137
scp ./postgresql/settings.env $host:/home/app/silkaudio/postgresql
scp ./web/settings.env $host:/home/app/silkaudio/web
# ssh do 'bash -s' < server.sh