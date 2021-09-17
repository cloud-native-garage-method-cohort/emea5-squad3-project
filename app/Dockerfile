FROM python:3.8-buster
RUN apt-get update 
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
COPY app/requirements.txt ./
RUN pip install -r requirements.txt
COPY app/ .
RUN python manage.py migrate
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
