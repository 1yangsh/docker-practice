FROM python:3.7.9-stretch

WORKDIR /mydjango
COPY bookmark /mydjango/bookmark
COPY mysite /mydjango/mysite
COPY db.sqlite3 /mydjango/db.sqlite3
COPY manage.py /mydjango/manage.py

RUN apt-get update
RUN pip install django
RUN pip install mysqlclient
RUN apt-get install -y vim


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]