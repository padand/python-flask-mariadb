## Prerequisites

- Docker compose (https://docs.docker.com/compose/install/)

## Start

```
sudo docker-compose up
```

Wait for everything to start, then test the api:

```
http://localhost:5000/api/people
```

## Useful

#### Start docker compose detached

```
sudo docker-compose up -d
```

#### Attach to container logs

```
sudo docker-compose logs -f
```

#### Start a fresh db seed

```
sudo docker-compose up seed
```

#### Connect to mariadb

Start a bash in the db container:

```
sudo docker-compose exec db bash
```

Connect to db:

```
mysql -u root -psupersecret
```

Or use this one liner:

```
sudo docker-compose exec db bash -c "mysql -u root -psupersecret"
```

Show us something in mysql client:

```
show databases;
use demo;
show tables;
select * from people;
```

#### If you need to use python locally

Make sure you have the correct version of python installed (check docker compose for the version).

Create a virtual environment for this app (you will do this once):

```
python3 -m venv ~/temp/python-flask-mariadb
```

Activate the environment (you will do this every time you start working on the project)

```
source ~/temp/python-flask-mariadb/bin/activate
```

Now, everything you install in python is limited to your virtual env.

Install requirements:

```
pip install -r app/requirements.txt
```

Run the app:

```
python3 app/api.py
```

Note: you may need to reconfigure the app for running local