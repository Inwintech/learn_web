from webapp.db import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)
    email = db.Column(db.Sring(50), unique=True)

    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)