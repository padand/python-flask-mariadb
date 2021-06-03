## Prerequisites

This project requires docker compose

```
https://docs.docker.com/compose/install/
```

## Start

```
sudo docker-compose up
```

## Useful

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