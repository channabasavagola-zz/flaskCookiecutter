from flask import Flask
from config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flaskApp.models import studentDemographics, db
from utils import initdb

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config.from_object(Config)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def createdb():
	# from utils
    initdb()

if __name__ == '__main__':
	manager.run()