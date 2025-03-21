from flask import Blueprint, render_template
from app.models import Article

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    articles = Article.query.order_by(Article.published_date.desc()).all()
    return render_template('index.html', articles=articles)

@bp.route('/article/<int:id>')
def article(id):
    article = Article.query.get_or_404(id)
    return render_template('article.html', article=article)