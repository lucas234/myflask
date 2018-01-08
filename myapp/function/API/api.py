# _*_ coding=utf-8 _*_
import requests
from params import *
import time
import json


def get_captcha_ticket():
    """
    :return: 获取图片验证码
    """
    response_img = requests.request("POST", url_img)
    # print response_img.json()
    if response_img.json()["code"] == 1000:
        captcha_ticket = response_img.json()["data"]["captcha_ticket"]
        return captcha_ticket
    else:
        print "获取图片验证码失败"
        return False


def get_sms_ticket(phone, img_code, captcha_ticket):
    """
    获取短信验证码
    :param phone:
    :param img_code:
    :param captcha_ticket: from get_captcha_ticket
    :return:
    """
    payload_sms = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: " \
                  "form-data; name=\"captcha\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: " \
                  "form-data; name=\"captcha_ticket\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: " \
                  "form-data; name=\"phone\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--" % (
                  img_code, captcha_ticket, phone)
    headers = {'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'}

    response_sms = requests.request("POST", url_sms, data=payload_sms, headers=headers)
    if response_sms.json()["code"] == 1000:
        sms_ticket = response_sms.json()["data"]["sms_ticket"]
        return sms_ticket
    else:
        print "获取短信验证码失败"
        print response_sms.text
        return False


def submit(phone, sms_code, sms_ticket):
    """
    提交注册
    :return: No
    """
    time.sleep(1)
    payload = {"phone": phone, "password": "123456", "code": sms_code, "sms_ticket": sms_ticket, "source": "11",
               "nickname": "", "recommendCode": ""}
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", url_sub, data=json.dumps(payload), headers=headers)
    if response.json()["code"] == 1000:
        return True, response.json()["data"]["userId"]
    else:
        return False, response
# phone = 17077786854
# img_code = 1234
# sms_code = 123456
# captcha_ticket = get_captcha_ticket()
# sms_ticket = get_sms_ticket(phone, img_code, captcha_ticket)
# print submit(phone, sms_code, sms_ticket)


def real_name(uid, cardNumber, realName):
    """
    实名认证
    :return:
    """
    payload = {"uid": uid, "cardNumber": cardNumber, "realName": realName}
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url_realname, data=json.dumps(payload), headers=headers)
    if response.json()["code"] == 1000:
        return response.json()["msg"]
    elif response.json()["code"] == 110001:
        # print response.text
        return False
    else:
        return response.text

# uid = "6354239999520538625"
# cardNumber = "320621198612269971"
# realName = u"方爱红"
# print real_name(uid, cardNumber, realName)


from functools import wraps


def decorator(func):
    @wraps(func)
    def decorator_func(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.json()["code"] == 1000:
            return response
        else:
            return response.text
    return decorator_func


# @decorator
# def test():
#     """
#     :return: 获取图片验证码
#     """
#     response_img = requests.request("POST", url_img)
#     return response_img
#
# print test().text
