# Dockerfile
FROM python:3.8
WORKDIR /app-service
COPY . /app-service
RUN pip install -r requirements.txt
EXPOSE 8090
