# _*_ coding=utf-8 _*_

from flask import render_template, Blueprint
admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    return render_template('index.html')

@admin.route('/hello')
def hello():
    return "1234"
