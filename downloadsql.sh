#!/bin/bash

host=root@138.68.178.137
scp -r $host:/home/app/silkaudio/postgresql/backup ./postgresql/
