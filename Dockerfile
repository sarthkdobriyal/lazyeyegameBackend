FROM python

WORKDIR /app

COPY . .

RUN . env/bin/activate

RUN pip install -r requirements.txt

EXPOSE 2223

RUN python manage.py runserver 127.0.0.1:2223


