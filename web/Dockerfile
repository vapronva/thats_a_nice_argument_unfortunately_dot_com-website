FROM docker.io/library/python:3.11-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip3 install Flask==2.3.3 gunicorn==21.2.0

ENTRYPOINT [ "gunicorn", "main:app" ]
CMD [ "--bind", "0.0.0.0:8000", "--workers", "6" ]
