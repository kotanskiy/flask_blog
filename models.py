from datetime import datetime
from app import database
import re


def slugify(string):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', string)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(140))
    slug = database.Column(database.String(140), unique=True)
    body = database.Column(database.Text)
    created = database.Column(database.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)
