from celery import Celery
from app import create_app
import feedparser
from bs4 import BeautifulSoup
import requests
from deepl import Translator
from app.models import Article
from datetime import datetime

app = create_app()
celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def parse_rss_feeds():
    feeds = [
        'https://towardsdatascience.com/feed',
        'https://venturebeat.com/feed/',
        'https://rss.app/feeds/PNcbNOcr3uiLMKOm.xml'
    ]
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            if not Article.query.filter_by(source_url=entry.link).first():
                article = Article(
                    title=entry.title,
                    summary=entry.summary,
                    content=get_full_content(entry.link),
                    source_url=entry.link,
                    published_date=datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z')
                )
                db.session.add(article)
                db.session.commit()
                translate_article.delay(article.id)

def get_full_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return str(soup.find('article') or soup.find('body'))

@celery.task
def translate_article(article_id):
    article = Article.query.get(article_id)
    translator = Translator(app.config['DEEPL_API_KEY'])
    article.translated_content = translator.translate_text(article.content, target_lang='RU').text
    db.session.commit()