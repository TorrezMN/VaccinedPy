
# DOCKERFILE API


FROM python:3.9


WORKDIR /code

COPY requirements.txt ./

RUN pip install --upgrade pip && apt-get update && apt-get -y install cron && apt-get -y install htop



RUN pip install -r requirements.txt



COPY . /code/


