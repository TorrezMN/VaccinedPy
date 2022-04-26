
# DOCKERFILE API



FROM python:3.9

WORKDIR /code

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN apt-get update && apt-get -y install cron && apt-get -y install htop


COPY . /code/


