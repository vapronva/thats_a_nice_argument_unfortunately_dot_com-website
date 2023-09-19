FROM docker.io/library/python:3.11-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip3 install Flask==2.3.3

CMD [ "python3", "main.py" ]
