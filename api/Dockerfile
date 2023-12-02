FROM docker.io/library/python:3.12-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "uvicorn", "main:app" ]

CMD [ "--host", "0.0.0.0", "--port", "8000", "--workers", "4" ]
