FROM python:3.10.11-slim-buster

USER root
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /camera-ip-capturing

COPY . .

# Install requirements
RUN pip3 install -r requirements.txt --no-cache-dir
