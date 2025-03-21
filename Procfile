web: gunicorn run:app
worker: celery -A worker.celery worker --loglevel=info --pool=eventlet
beat: celery -A worker.celery beat --loglevel=info