import feedparser
import deepl
from celery import Celery
from celery.schedules import crontab
from app.models import Article
from config import Config
from app import db

def configure_celery(app):
    celery = Celery(
        'app',
        broker=Config.broker_url,
        backend=Config.result_backend,
        include=['app.tasks']
    )

    celery.conf.update(
        beat_schedule={
            'parse-rss-every-5-minutes': {
                'task': 'app.tasks.parse_and_translate_rss',
                'schedule': crontab(minute='*/5'),  # Каждые 5 минут
            },
        },
        timezone='UTC',
        broker_connection_retry_on_startup=True
    )

    # Устанавливаем контекст приложения для Celery
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    @celery.task
    def parse_and_translate_rss():
        feed_url = "https://towardsdatascience.com/feed"
        feed = feedparser.parse(feed_url)
        
        translator = deepl.Translator(Config.DEEPL_API_KEY)
        
        for entry in feed.entries:
            # Проверяем, существует ли статья в базе данных
            existing_article = Article.query.filter_by(link=entry.link).first()
            if existing_article:
                continue
            
            # Переводим заголовок и описание
            title = translator.translate_text(entry.title, target_lang="RU").text
            summary = translator.translate_text(entry.summary, target_lang="RU").text
            
            # Сохраняем статью в базу данных
            article = Article(
                title=title,
                summary=summary,
                link=entry.link,
                published_date=entry.published_parsed
            )
            db.session.add(article)
        
        db.session.commit()
        print(f"Processed {len(feed.entries)} articles from {feed_url}")

    return celery