FROM python:3.10.11-slim-buster

USER root
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean && apt-get autoclean && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /camera-ip-capturing

COPY . .

# Install requirements
RUN pip3 install -r requirements.txt --no-cache-dir
