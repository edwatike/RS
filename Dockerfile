FROM python:3.10-slim

# Устанавливаем git
RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]