## Сборка проекта
1. Установка virtualenv:

    $ pip3 install virtualenv
    
2. Создание окружения в папке с проектом:

    $ virtualenv env
    
3. Запуск virtualenv:

    $ source env/bin/activate
    
4. Установка Django:

    $ pip3 install django
    
5. Установка сервера и консольного клиента MySQL:

    $ sudo apt-get install mysql-server mysql-client
    
6. Запуск консольного клиента MySQL:

    $ mysql -u root -p
7. Создание БД:

    mysql> CREATE DATABASE MD5light_db DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
    
8. Создание отдельного пользователя для Django в MySQL:

    mysql> CREATE USER DB_user@localhost IDENTIFIED BY password;
    mysql> GRANT ALL PRIVILEGES ON MD5light_db.* TO DB_user@localhost;
    mysql> FLUSH PRIVILEGES;
    
9. Нажмите Ctrl-D для выхода из консольного клиента MySQL.

10. Установка библиотек и пакетов, необходимых для работы с MySQL из Python:

    $ pip install mysqlclient
    
11. Проведите миграции в Django:

    $ ./manage.py migrate
    
12. Ставим Celery:

    $ pip install Celery
    
13. Ставим Redis:

    $ pip install redis
    
14. Ставим Django File Md5:

    $ pip install django-file-md5
    
15. Для запуска проекта выполните команду:

    $ ./manage.py runserver
    
16. Запустите Redis сервер в отдельной консоли следующим образом:

    $ redis-server
    
17. Запустим Celery в отдельной консоли:

    $ celery worker -A MD5light --loglevel=INFO
    