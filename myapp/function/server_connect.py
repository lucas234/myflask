# _*_ coding=utf-8 _*_
import paramiko
from config import *
import MySQLdb
import redis


class ServerConnect(object):
    def __init__(self):
        # self.ssh_host = config_name.get("host", None)
        # self.ssh_port = config_name.get("port", None)
        # self.ssh_user = config_name.get("flaskr", None)
        # self.ssh_key = config_name.get("key", None)
        # self.ssh_psw = config_name.get("password", None)

        # pkey = paramiko.RSAKey.from_private_key_file(self.ssh_key)
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            # self.ssh.connect(self.ssh_host, self.ssh_port, self.ssh_user, self.ssh_psw, pkey=pkey)
            self.ssh.connect(**test)
        except Exception as e:
            print "connect server fail， please have a check!"
            print e

    def closed(self):
        self.ssh.close()

    def command(self, args, outpath):
        'this is get the command the args to return the command'
        cmd = '%s %s' % (outpath, args)
        return cmd

    def exec_commands(self, cmd):
        'this is use the conn to excute the cmd and return the results of excute the command'
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        results = stdout.read()
        return results


class DataBaseConnection:
    def __init__(self):
        self.conn = MySQLdb.connect(**mysql_config_192)
        self.cursor = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        self.cursor.execute("set names 'utf8'")  # 解决中文显示乱码
        # conn = MySQLdb.connect(host=mysql_config.get("host"), port=mysql_config.get("port"),
        #                        flaskr=mysql_config.get("flaskr"), passwd=mysql_config.get("password"),
        #                        db=mysql_config.get("db"))

    def select(self, sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            # conn.commit()
            return data
        except Exception as msg:
            print msg
            self.conn.rollback()

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.cursor.fetchall()
            self.conn.commit()
        except Exception as msg:
            print msg
            self.conn.rollback()

    def closed(self):
        self.cursor.close()
        self.conn.close()

# db = DataBaseConnection()
# temp = db.select("select * from realname where status=2 limit 1")
# print temp[0].get("card_id"), temp[0].get("nickname")


class RedisConnection:

    def __init__(self):
        # r = redis.Redis(**redis_config)
        self.pool = redis.ConnectionPool(**redis_config)
        self.r = redis.Redis(connection_pool=self.pool)

    def set(self, key, value):
        return self.r.set(key, value)

    def get(self, key):
        return self.r.get(key)

    def remove(self, key):
        return self.r.delete(key)

    def expire(self, key):
        return self.r.expire(key, 100)
