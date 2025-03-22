class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12059001@db:5432/rss_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    broker_url = 'redis://redis:6379/0'  # Обновлено
    result_backend = 'redis://redis:6379/0'  # Обновлено
    DEEPL_API_KEY = '49a435b1-7380-4a48-bf9d-11b5db85f42b:fx'