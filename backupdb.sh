#!/bin/bash

docker exec -t silkaudio_postgres_1 pg_dumpall -c -U postgres > ./postgresql/backup/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql