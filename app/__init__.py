from flask import Flask
import os

app = Flask(__name__)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


app.config.from_object(Config)

from app import routes
