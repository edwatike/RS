from flask import render_template, current_app
from app.models import Article

def register_routes(app):
    @app.route('/')
    def index():
        with app.app_context():
            articles = Article.query.order_by(Article.published_date.desc()).all()
        return render_template('index.html', articles=articles)