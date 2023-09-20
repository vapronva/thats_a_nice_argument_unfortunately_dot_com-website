FROM docker.io/library/python:3.11-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip3 install Flask==2.3.3 uvicorn==0.23.2

ENTRYPOINT [ "uvicorn", "main:app" ]
CMD [ "--host", "0.0.0.0", "--port", "8000", "--workers", "4" ]
