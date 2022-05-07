# VaccinedPy

## About 
This is a project that uses the open data bank of vaccinated people in Paraguay. It provides a series of utilities that allow easy and effective access to them.


## Stack
For the development of this project the following tools are used.
- [docker-compose](https://docs.docker.com/compose/) Provides support for containers orchestration.
- [FastApi](https://fastapi.tiangolo.com/) : It provides a series of endpoints that allow you to explore the recorded data.
- [PostgreSql](https://www.postgresql.org/) : Provides support for data persistence within the application.
- [Dagster](https://dagster.io/) : The data orchestration platform. Provides support for data ETL automation and automated tasks within the project.
- ***Python Libraries***
  - sqlalchemy
  - pandas
  - dash


## How is this project organized?

### API

### Web 

### ETL

## How to Run

  First you need to clone this project.

```
git clone https://github.com/TorrezMN/VaccinedPy.git
```

then go in to "VaccinedPy"

```
cd VaccinedPy/
```

then run the project with docker-compose:

```
sudo docker-compose up
```
***Only the first time.***
You must enter the Dagster task manager and fire the initial data load task. For this go to:

```
http://0.0.0.0:3000
```
In the upper left corner you will see a tab that says ***"launchpad"***. Click there.
![dagster_home](https://github.com/TorrezMN/VaccinedPy/blob/main/docs/foto1.png)


The task graph view appears. At the bottom right you will see a button that says ***"Launch run"***. click there and you will see the ETL process running.
![dagster_home](https://github.com/TorrezMN/VaccinedPy/blob/main/docs/foto2.png)

After this step, you have 3 options.

  - [API Home](http://0.0.0.0:8000)
  - [Web Dashboard](http://0.0.0.0:5000/)
  - [Dagger Manager](http://0.0.0.0:3000)


API Home
```
  http://0.0.0.0:8000
```
Web Dashboard

```
http://0.0.0.0:5000/
```

Dagger Manager


```
http://0.0.0.0:3000
```


