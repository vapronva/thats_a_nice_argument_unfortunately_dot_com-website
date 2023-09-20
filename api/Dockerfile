FROM docker.io/library/python:3.11-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip3 install fastapi==0.103.1 Faker==19.6.1 typing_extensions==4.8.0 requests==2.31.0 pydantic==2.3.0 uvicorn==0.23.2 pymongo==4.5.0

CMD [ "python3", "main.py" ]
