FROM python:3.10-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip3 install fastapi==0.72.0 Faker==11.3.0 typing_extensions==4.0.1 requests==2.26.0 pydantic==1.8.2 uvicorn==0.17.0

CMD [ "python3", "main.py" ]
