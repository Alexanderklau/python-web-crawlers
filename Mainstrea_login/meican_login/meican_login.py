# coding: utf-8

__author__ = 'Yemilice_lau'

import json
import requests
import http.cookiejar as HC
import datetime


session = requests.session()
session.cookies = HC.LWPCookieJar(filename='cookies')

def login_meican():
    """
    登录美餐，寻找cookie文件，没cookie文件就重新载入
    :return:
    """
    # 储存cookie作为日后使用，三天clear一次
    try:
        session.cookies.load(ignore_discard=True)
    except:
        print('未找到cookies文件')
        save_cookie()

def save_cookie():
    login_url = 'https://meican.com/account/directlogin'

    # Headers
    hearsers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        "Referer": "https://meican.com/login",
        "Origin": "https://meican.com",
        "Host": "meican.com",
        "Accept": "*/*"
    }

    # Login need data

    data = {
        "username": "xxxxxxxxxxxxxx",
        "loginType": "username",
        "password": "xxxxxxxxxxxxx",
        "remember": "true"
    }

    try:
        r = session.post(login_url, headers=hearsers, data=data)
        r.raise_for_status()
        session.cookies.save()
    except Exception as e:
        print("login error!")
        return 0


def get_menu():
    pass


def order_action():
    pass



def get_for_my_order():
    """
    找到今天点了什么餐
    :return:
    """
    Now_date = datetime.date.today()
    z = session.get("https://meican.com/preorder/api/v2.1/calendaritems/list?withOrderDetail=false&beginDate={Now}&endDate={Now}".format(Now=Now_date))
    print(json.loads(z.text))

login_meican()
get_for_my_order()