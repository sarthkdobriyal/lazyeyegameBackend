# Lazy eye game

## Running backend
 - install python and pip
 - run virtual env ->  `source env/bin/activate`
 - install requirements -> `pip install -r requirements.txt`
 - make migrations ->  `python3 manage.py makemigrations`
 - migrate scheams to db ->  `python3 manage.py migrate_schemas`
 - create super user ->  `python3 manage.py createsuperuser`
 - run dev server -> `python3 manage.py runserver 127.0.0.1:2222`
 - run prod server -> `gunicorn --bind 127.0.0.1:2222 server.wsgi`

 ## Access pgadmin4 (Always running)
    -> goto -> http://localhost:8081/pgadmin4
    -> admin@leg.com:admin123

## Credentials
    - admin --> admin:qwerty
    - doctor/patient --> doc1:1234 or doc1p1:1234