## Сборка проекта
1. Установка virtualenv:
```sh
    $ pip3 install virtualenv
```
2. Создание окружения в папке с проектом:
```sh
    $ virtualenv env
```
3. Запуск virtualenv:
```sh
    $ source env/bin/activate
```
4. Установка Django:
```sh
    $ pip3 install django
```    
5. Установка сервера и консольного клиента MySQL:
```sh
    $ sudo apt-get install mysql-server mysql-client
```    
6. Запуск консольного клиента MySQL:
```sh
    $ mysql -u root -p
```
7. Создание БД:
```sh
    mysql> CREATE DATABASE MD5light_db DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
```    
8. Создание отдельного пользователя для Django в MySQL:
```sh
    mysql> CREATE USER DB_user@localhost IDENTIFIED BY password;
    mysql> GRANT ALL PRIVILEGES ON MD5light_db.* TO DB_user@localhost;
    mysql> FLUSH PRIVILEGES;
```
9. Нажмите Ctrl-D для выхода из консольного клиента MySQL.

10. Установка библиотек и пакетов, необходимых для работы с MySQL из Python:
```sh
    $ pip install mysqlclient
```    
11. Проведите миграции в Django:
```sh
    $ ./manage.py migrate
```    
12. Ставим Celery:
```sh
    $ pip install Celery
```    
13. Ставим Redis:
```sh
    $ pip install redis
```    
14. Для запуска проекта выполните команду:
```sh
    $ ./manage.py runserver
```    
15. Запустите Redis сервер в отдельной консоли следующим образом:
```sh
    $ redis-server
```    
16. Запустим Celery в отдельной консоли:
```sh
    $ celery worker -A MD5light --loglevel=INFO
```    