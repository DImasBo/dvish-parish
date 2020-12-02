#!/bin/bash

cd app/
git pull
echo "hello world"
docker-compose -f production.yml up -d --build
