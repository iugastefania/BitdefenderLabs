FROM python:3.8-slim-bullseye

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV TZ=Europe/Bucharest
ENV PYTHONPATH=/app


RUN pip install -r events-api/requirements.txt

CMD python /app/events-api/main.py