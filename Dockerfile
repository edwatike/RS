FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libgdbm-dev \
    libgdbm-compat-dev \
    git

WORKDIR /app

# Обновляем pip до последней версии
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --timeout 1000

COPY . .    