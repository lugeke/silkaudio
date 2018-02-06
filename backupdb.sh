#!/bin/bash
cd /home/app/silkaudio/postgresql/backup &&
docker exec -t silkaudio_postgres_1 pg_dumpall -c -U postgres > ./dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql