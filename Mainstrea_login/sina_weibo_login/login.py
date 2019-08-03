# coding: utf-8

__author__ = 'lau.wenbo'

"""
login sina weibo
"""

import json

import requests


session = requests.session()

def login_sina():
    """
    login sina code
    :return:
    """

    login_url = 'https://passport.weibo.cn/sso/login'

    # Headers
    hearsers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        "Referer":"https://passport.weibo.cn/signin/login?display=0&retcode=6102",
        "Origin":"https://passport.weibo.cn",
        "Host":"passport.weibo.cn",
        "Accept":"*/*"
    }

    # Login need data

    data = {
        "username": "",
        "password": "",
        "savestate": 1,
        "entry": "mweibo",
        "mainpageflag": 1
    }

    try:
        r = session.post(login_url, hearsers=hearsers, data=data)
        r.raise_for_status()
    except:
        print("login error!")
        return 0

    print(json.loads(r.text)['msg'])
    return 1
