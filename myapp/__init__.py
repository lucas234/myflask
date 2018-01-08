# _*_ coding=utf-8 _*_
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

DEBUG = True
SECRET_KEY = 'development key'
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from myapp import models, views


# admin = Blueprint('admin', __name__)
flaskr = Blueprint('flaskr', __name__)
