from datetime import datetime
from app import database
import re


def slugify(string):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', str(string))


post_tags = database.Table(
    'post_tags',
    database.Column('post_id', database.Integer, database.ForeignKey('post.id')),
    database.Column('tag_id', database.Integer, database.ForeignKey('tag.id'))
)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(140))
    slug = database.Column(database.String(140), unique=True)
    body = database.Column(database.Text)
    created = database.Column(database.DateTime, default=datetime.now())
    tags = database.relationship('Tag', secondary=post_tags, backref=database.backref('posts'), lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '{}'.format(self.title)


class Tag(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100))
    slug = database.Column(database.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '{}'.format(self.name)

