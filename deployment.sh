#!/bin/bash

docker-compose -f /home/ubuntu/backend-runtime/docker-compose.yml down
docker-compose -f /home/ubuntu/backend-runtime/docker-compose.yml pull
docker-compose -f /home/ubuntu/backend-runtime/docker-compose.yml up -d
