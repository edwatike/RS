from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Инициализация SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Инициализация SQLAlchemy
    db.init_app(app)
    
    # Регистрация моделей
    with app.app_context():
        from app import models
        db.create_all()
    
    return app