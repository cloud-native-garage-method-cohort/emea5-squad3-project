FROM python:3.8-buster

RUN apt-get update 

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV DJANGO_SUPERUSER_USERNAME=squad3admin
ENV DJANGO_SUPERUSER_PASSWORD=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@admin.com

COPY app/requirements.txt ./

RUN pip install -r requirements.txt

COPY app/ .

USER root
RUN chgrp root . && chmod g+w .

EXPOSE 8080
CMD ["./runserver.sh"]
