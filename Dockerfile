# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

ENV PYTHONPATH=.

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "src/main.py" ]