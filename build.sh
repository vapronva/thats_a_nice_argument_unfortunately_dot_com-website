#!/bin/bash
set -e
cd api/
docker build -t thats-a-nice-argument-unfortunately-dot-com-api:${CI_COMMIT_SHA} .
cd ../
docker-compose -f 'docker-compose.yml' --project-name 'wa-tnauc' down
docker-compose -f 'docker-compose.yml' --project-name 'wa-tnauc' up -d
