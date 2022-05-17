# Dockerfile
FROM python:3

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dependencies를 위한 apt-get update
RUN apt-get update && apt-get -y install \
    libpq-dev --no-install-recommends apt-utils

# django application 작업 공간
WORKDIR /app
COPY . /app

COPY requirements.txt ./
RUN pip install --upgrade pip && pip3 install -r requirements.txt




# EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]