from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    summary = db.Column(db.Text)
    content = db.Column(db.Text)
    translated_content = db.Column(db.Text)
    source_url = db.Column(db.String(255))
    published_date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Article {self.title}>'