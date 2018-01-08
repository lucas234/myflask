# coding: utf-8
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Api(Base):
    __tablename__ = 'api'

    id = Column(Integer, primary_key=True)
    ip = Column(String(255))
    param = Column(String(255))
    status = Column(String(1), server_default=text("'1'"))
    delete_flag = Column(String(1), server_default=text("'1'"))


class Config(Base):
    __tablename__ = 'config'

    id = Column(Integer, primary_key=True)
    host = Column(String(50))
    port = Column(String(20))
    user = Column(String(50))
    key = Column(String(50))
    passwd = Column(String(50))
    password = Column(String(50))
    db = Column(String(20))
    hostname = Column(String(50))
    username = Column(String(50))
    status = Column(Integer)


class Realname(Base):
    __tablename__ = 'realname'

    id = Column(Integer, primary_key=True)
    card_id = Column(String(20), nullable=False)
    nickname = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    type = Column(Integer, nullable=False, server_default=text("'0'"))
