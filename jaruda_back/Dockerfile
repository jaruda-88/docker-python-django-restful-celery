# Dockerfile
FROM python:3

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Avoiding user interaction with tzdata
ENV DEBIAN_FRONTEND=noninteractive

# dependencies를 위한 apt-get update
RUN apt-get update && apt-get -y install \
    libpq-dev --no-install-recommends apt-utils

# django application 작업 공간
WORKDIR /app
COPY . /app

# 리콰이어먼트
COPY requirements.txt ./
RUN pip install --upgrade pip && pip3 install -r requirements.txt

# django runserver
# CMD ["/bin/bash", "run.sh"]
# 슈퍼바이저 api 서버 container에 app하고 celery 동시 실행
# RUN apt-get install supervisor -y
# COPY supervisord.conf ./
# CMD ["/usr/bin/supervisord"]
# RUN mkdir -p /app/logs
# CMD ["supervisord", "-c", "supervisord.conf"]

