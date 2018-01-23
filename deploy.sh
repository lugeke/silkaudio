#!/bin/bash

ssh vps 'cd /home/jiaheng/flask/silkaudio && git pull origin master && sudo systemctl restart silkaudio'  

