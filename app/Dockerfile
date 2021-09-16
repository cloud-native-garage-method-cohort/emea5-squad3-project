FROM python:3.10
RUN apt-get update 
WORKDIR /usr/src/app
COPY requirements ./
RUN pip install -r requirements
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]