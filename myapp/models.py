# _*_ coding=utf-8 _*_
from myapp import db


class RealName(db.Model):
    __table_args__ = {'extend_existing': True, 'mysql_charset': 'utf8'}
    __tablename__ = 'realname'

    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'card_id': self.card_id,
            'nickname': self.nickname,
            'status': self.status
            }

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

# insert values
# inset = RealName(card_id='12345678910', nickname='itmin@qq.com', status=33)
# db.session.add(inset)
# db.session.commit()

# update values
# news = RealName.query.all()
# print news
# news[1].nickname = 'test'
# db.session.commit()

# delete values
# name=User.query.filter_by(username = 'bb').first()
# db.session.delete(name)
# db.session.commit()

# select values
# select_ = RealName.query.limit(1)
# print select_[0].to_json()  # 查询结果转化为json的两种方法
# print select_[0].to_dict()
# temp = []
# for x in select_:
#     temp.append(x.to_json())
# print temp
# print (select_[0].__table__.columns) # 精确查询，并查找出ID
# print getattr(select_, .name)
# print User.query.filter(User.email.endswith('@qq.com')).all()  # 模糊查询
# print User.query.filter(User.phone.endswith('13812345678')).all()
# print User.query.filter(User.username != 'yoyo').first()  # 反条件查询，非
# print User.query.filter(not_(User.username == 'yoyo')).first()
# print User.query.filter(or_(User.username != 'yoyo', User.email.endswith('@example.com'))).first()  # 或查询
# print User.query.filter(and_(User.username != 'yoyo', User.email.endswith('@example.com'))).first()  # 与查询
# print User.query.limit(10).all()  # 查询返回的数据的数目
# data_all = User.query.all()
# print (data_all)  # 查询全部
#
# for i in range(len(data_all)):
#     print data_all[i].username + " " + data_all[i].email + " " + data_all[i].phone