FROM python:3

COPY requirements.txt ./
RUN apt-get update
RUN apt-get install -y
RUN pip install --upgrade pip
RUN pip install mysqlclient
RUN pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

# EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]