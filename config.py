from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEEPL_API_KEY = os.environ.get('DEEPL_API_KEY')
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    result_backend = os.environ.get('CELERY_RESULT_BACKEND')  # Используем новое имя настройки