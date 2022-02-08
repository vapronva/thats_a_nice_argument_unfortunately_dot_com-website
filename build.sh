#!/bin/bash
set -e
docker-compose -f 'docker-compose.yml' --project-name 'wa-tnauc' down
docker build -t thats-a-nice-argument-unfortunately-dot-com-api .
docker-compose -f 'docker-compose.yml' --project-name 'wa-tnauc' up -d
