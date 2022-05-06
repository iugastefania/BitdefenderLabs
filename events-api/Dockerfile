FROM python:3.8-slim-bullseye

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV TZ=Europe/Bucharest

RUN pip install -r events_api/requirements.txt

CMD python /app/events_api/main.py