import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgresql:12059001@localhost:5432/rss_db?client_encoding=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEEPL_API_KEY = '49a435b1-7380-4a48-bf9d-11b5db85f42b:fx'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'