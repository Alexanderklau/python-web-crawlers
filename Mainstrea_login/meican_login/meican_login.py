# coding: utf-8

__author__ = 'Yemilice_lau'

import json
import requests
import http.cookiejar as HC
import datetime
from random import choice
import copy

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
    """
    如果没cookie，登录逻辑
    :return:
    """
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
        "username": "xxxxxxxxxxxxxxxxxxx",
        "loginType": "username",
        "password": "xxxxxxxxxxxx",
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
    """
    获取餐单逻辑
    :return:
    """
    menu_dict = {}
    menu_list = []
    Now_date = datetime.date.today()
    uuid = get_for_my_order()["uuid"]
    z = session.get("https://meican.com/preorder/api/v2.1/recommendations/dishes?tabUniqueId={uuid}&targetTime={Now}+09:40".format(uuid = uuid, Now=Now_date))
    menu = json.loads(z.text)["myRegularDishList"]
    for i in menu:
        menu_dict["id"] = i["id"]
        menu_dict["name"] = i["name"]
        z = copy.deepcopy(menu_dict)
        menu_list.append(z)
    return menu_list



def order_action():
    """
    点餐逻辑
    :return:
    """
    addrid = get_for_my_order()["addrid"]
    uuid = get_for_my_order()["uuid"]
    menu_list = get_menu()
    menu_id = choice(menu_list)["id"]
    target_time = str(datetime.date.today()) + " " + "09:40"

    data = {
        "corpAddressRemark":"",
        "corpAddressUniqueId": addrid,
        "order": [{"count":1,"dishId":menu_id}],
        "remarks": [{"dishId":menu_id,"remark":""}],
        "tabUniqueId": uuid,
        "targetTime":target_time,
        "userAddressUniqueId":addrid
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    try:
        z = session.post("https://meican.com/preorder/api/v2.1/orders/add", headers=headers, data=data)
        z.raise_for_status()
    except:
        return "点餐错误！"

def get_for_my_order():
    """
    找到usertorken, addrid
    :return:
    """
    user_dict = {}
    Now_date = datetime.date.today()
    z = session.get("https://meican.com/preorder/api/v2.1/calendaritems/list?withOrderDetail=false&beginDate={Now}&endDate={Now}".format(Now=Now_date))
    x = json.loads(z.text)
    user_dict["uuid"] = x["dateList"][0]["calendarItemList"][0]["userTab"]["uniqueId"]
    user_dict["addrid"] = x["dateList"][0]["calendarItemList"][0]["userTab"]["corp"]["addressList"][0]["uniqueId"]
    return user_dict


if __name__ == '__main__':
    login_meican()
    print(order_action())