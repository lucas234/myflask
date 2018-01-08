# _*_ coding=utf-8 _*_

from myapp import app
# from myapp.admin import admin
from myapp.flaskr import flaskr


# app.register_blueprint(admin)
app.register_blueprint(flaskr)


