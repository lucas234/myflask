# _*_ coding=utf-8 _*_

# 从数据库生成model
# sqlacodegen --noviews --noconstraints --noindexes --outfile H:\study\FLASK\testmodels.py mysql://root:123456@192.168.40.192:3306/testtools

SQLALCHEMY_DATABASE_URI = "mysql://root:123456@XXXXXX:3306/testtools?charset=utf8"  # 'mysql+pymysql://root:xxxxx@localhost:3306/test?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
