FROM python:3.7.9-stretch

WORKDIR /mydjango

RUN pip install django
RUN pip install mysqlclient

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]