#!/bin/bash
cd /home/app/silkaudio/postgresql && mkdir -p backup && cd backup && 
docker exec -t silkaudio_postgres_1 pg_dumpall -c -U postgres > ./dump_`date +%Y-%m-%d"_"%H_%M_%S`.sql