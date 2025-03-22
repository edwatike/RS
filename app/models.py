from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    translated_title = db.Column(db.String(255), nullable=False)
    translated_content = db.Column(db.Text, nullable=False)
    published_date = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f"<Article {self.title}>"