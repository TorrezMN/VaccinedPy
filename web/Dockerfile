
# DOCKERFILE WEB

FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . /code/web/


CMD gunicorn --workers=5 --threads=1 -b 0.0.0.0:80 app:server
