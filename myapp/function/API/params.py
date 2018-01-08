# _*_ coding=utf-8 _*_

from urlparse import urljoin
host = "http://192.168.40.10"
url_img = urljoin(host, "/register/captcha")
url_sms = urljoin(host, "/register/sms")
url_sub = urljoin(host, "/register/submit")
url_realname = urljoin(host, "/flaskr/realName")