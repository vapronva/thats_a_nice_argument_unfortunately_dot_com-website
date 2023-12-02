FROM docker.io/library/python:3.12-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt 

ENTRYPOINT [ "gunicorn", "main:app" ]

CMD [ "--bind", "0.0.0.0:8000", "--workers", "6" ]
