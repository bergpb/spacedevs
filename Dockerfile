FROM python:3.7-slim

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt
