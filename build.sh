#!/bin/bash
set -e
cd api/
docker build -t thats-a-nice-argument-unfortunately-dot-com-api:${CI_COMMIT_TAG:-$CI_COMMIT_SHA} .
cd ../
cd web/
docker build -t thats-a-nice-argument-unfortunately-dot-com-web:${CI_COMMIT_TAG:-$CI_COMMIT_SHA} .
cd ../
IMAGE_VERSION=${CI_COMMIT_TAG:-$CI_COMMIT_SHA} docker-compose -f 'docker-compose.yml' --project-name 'wa-tnauc' down
IMAGE_VERSION=${CI_COMMIT_TAG:-$CI_COMMIT_SHA} docker-compose -f 'docker-compose.yml' --project-name 'wa-tnauc' up -d
