# FSA (FastApi + SQLAlchemy + Alembic)

Запуск 
````
$ docker-compose up -d --build
````
Используйте 127.0.0.0:8090/docs
![alt text](FSA.png)

Тесты 
````
$ docker-compose exec app python -m pytest app/tests
````
