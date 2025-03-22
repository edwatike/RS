from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery

db = SQLAlchemy()
migrate = Migrate()

def create_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)
    return celery

def create_app():
    app = Flask(__name__)

    # Конфигурация базы данных
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12059001@db:5432/rss_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Конфигурация Celery
    app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)

    # Создание объекта Celery
    celery = create_celery(app)
    app.celery = celery

    # Регистрация маршрутов
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Создание таблиц
    with app.app_context():
        db.create_all()

    return app