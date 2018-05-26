from flask import Flask
from flask_script import Manager

from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object(Configuration)


database = SQLAlchemy(app)

migrate = Migrate(app, database)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

import views
