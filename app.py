from flask import Flask
from flask_admin.contrib.sqla import ModelView
from flask_script import Manager

from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin


app = Flask(__name__)
app.config.from_object(Configuration)


database = SQLAlchemy(app)

migrate = Migrate(app, database)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import *

admin = Admin(app)
admin.add_view(ModelView(Post, database.session))
admin.add_view(ModelView(Tag, database.session))

import views
