FROM python:3.8-slim-bullseye

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV TZ=Europe/Bucharest

RUN pip install -r filesapi/requirements.txt

CMD python /app/filesapi/main.py