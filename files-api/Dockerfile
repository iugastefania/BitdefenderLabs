FROM python:3.8-slim-bullseye

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV TZ=Europe/Bucharest

RUN pip install -r files_api/requirements.txt

CMD python /app/files_api/main.py