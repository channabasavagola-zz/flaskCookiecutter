from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flaskApp import routes, models
from flaskApp.models import studentDemographics, db
from utils import initdb

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config.from_object(Config)

# db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))

@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """
    initdb()
    # db.create_all()
    # db.session.commit()

if __name__ == '__main__':
	manager.run()