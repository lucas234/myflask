# _*_ coding=utf-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Blueprint, request, session, redirect, url_for, abort, render_template, flash
from myapp.function.API.api import *
from myapp.function.server_connect import *
flaskr = Blueprint('flaskr', __name__)


@flaskr.route('/add_debt', methods=['GET', 'POST'])
def add_debt():
    product = {u"零活宝": "10", u"定期宝30天": "11", u"定期宝90天": "12", u"定期宝180天": "13", u"定期宝360天": "14", }
    payback = {u"先息后本": "2", u"等本等息": "3", u"等额本息": "4", u"等额本金": "5", u"月息季本": "6", u"混合方式": "24",}
    rate = {"10": 0.065, "11": 0.07, "12": 0.08, "13": 0.09, "14": 0.1,}
    sh = ServerConnect()
    msg = ''
    if request.method == 'POST':
        amount = request.form['amount']
        _id = request.form['borrow_id']
        borrow_days = request.form['borrow_days']
        pay_back = request.form['pay_back']
        p_items = request.form['p_items']
        first_cmd = "cd /data/www/saas-huolicai && php artisan  test:debtFillin -l %s -a %s -p %s -r %s -u %s | tr -cd '0-9'" % \
              (borrow_days, amount, pay_back, rate[p_items], _id)
        ti_id = sh.exec_commands(first_cmd)
        second_cmd = "cd /data/www/saas-huolicai && php artisan  test:debtOnline  -p %s -d %s" % (p_items, ti_id)
        msg = sh.exec_commands(second_cmd)
    sh.closed()
    return render_template('add_debt.html', output_log=msg, arr=sorted(product.items(), key=lambda d: d[1]),
                           payback=sorted(payback.items(), key=lambda d: d[1]))


@flaskr.route('/update_time', methods=['GET', 'POST'])
def update_time():
    # error = None
    sh = ServerConnect()
    msg = ''
    if request.method == 'POST':
        _date = request.form['chdate']
        cmd = "sudo date -s '%s'" % _date
        msg = sh.exec_commands(cmd)
    sh.closed()
    return render_template('update_time.html', output_log=msg)


@flaskr.route('/redis_key', methods=['GET', 'POST'])
def redis_key():
    _redis = RedisConnection()
    msg = ""
    if "set" in request.form.values():
        temp = request.form["keys"].split("-")
        msg = _redis.set(temp[0], temp[1])
    if "get" in request.form.values():
        msg = _redis.get(request.form["keys"])
    if "del" in request.form.values():
        msg = _redis.remove(request.form["keys"])
    return render_template('update_redis.html', output_log=msg)


@flaskr.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@flaskr.route('/hello')
def hello():
    return render_template('hello.html')


@flaskr.route('/register', methods=['GET', 'POST'])
def register():
    msg = ""
    dbs = DataBaseConnection()
    if request.method == 'POST':
        # print request.form.values()
        phone = request.form["phone"]
        realname = request.form.get("realname")
        img_code = request.form["captcha_img"]
        sms_code = request.form["captcha_sms"]
        captcha_ticket = get_captcha_ticket()
        sms_ticket = get_sms_ticket(phone, img_code, captcha_ticket)
        flag, uid = submit(phone, sms_code, sms_ticket)
        if realname and flag:
            while True:
                temp = dbs.select("select * from realname where status=0 limit 1")
                card_id = temp[0].get("card_id")
                nickname = temp[0].get("nickname")
                result = real_name(uid, card_id, nickname)
                dbs.execute("update realname set status = 1 where card_id = '%s' " % card_id)
                if result:   # 该身份证号未被实名，
                    msg = result
                    break
        else:
            msg = uid if flag else uid.text
    dbs.closed()
    return render_template('register.html', output_log=msg)


@flaskr.route('/recharge', methods=['GET', 'POST'])
def recharge():
    msg = ""
    # print request.form.values()
    if "查询" in request.form.values():
        phone = request.form.get("phone", None)
        msg = phone
    if "充值" in request.form.values():
        msg = request.form.get("amount", None)
    return render_template("recharge.html", output_log=msg)


