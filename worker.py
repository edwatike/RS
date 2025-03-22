from app import create_app
from app.tasks import configure_celery

app = create_app()
celery = configure_celery(app)

if __name__ == '__main__':
    celery.start()