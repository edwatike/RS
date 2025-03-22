from app import create_app

app = create_app()
celery = app.celery

# Пример задачи
@celery.task
def example_task():
    print("Example task is running!")