#!/bin/bash

docker-compose /home/ubuntu/backend-runtime down
docker-compose /home/ubuntu/backend-runtime pull
docker-compose /home/ubuntu/backend-runtime up -d
