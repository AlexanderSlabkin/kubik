import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



from config import Config


my_app = Flask(__name__)
my_app.config.from_object(Config)
db = SQLAlchemy(my_app)
migrate = Migrate(my_app, db)
login = LoginManager(my_app)
login.login_view = 'my_login'

if my_app.config['LOG_TO_STDOUT']:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    my_app.logger.addHandler(stream_handler)
else:
    if not os.path.exists('logs'):
        os.mkdir('logs')
        file_handler = RotatingFileHandler(
                                           'logs/egg_cracker.log',
                                            maxBytes=10240,
                                            backupCount=10
                                            )
        my_app.logger.addHandler(file_handler)
        my_app.logger.info('Egg Startup')
from egg_break import routes, models
