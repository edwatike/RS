FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libgdbm-dev \
    libgdbm-compat-dev \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Устанавливаем wait-for-it
RUN wget -O wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x wait-for-it.sh

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --timeout 1000

COPY . .