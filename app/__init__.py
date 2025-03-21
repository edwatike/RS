from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Инициализация расширений
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализация базы данных
    db.init_app(app)

    # Импорт и регистрация маршрутов
    from app import routes
    app.register_blueprint(routes.bp)

    return app