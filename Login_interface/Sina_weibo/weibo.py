# -*-coding:utf-8 -*-
__author__ = 'Yemilice_lau'
import json
import base64
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
"""
输入你的微博账号和密码，可去淘宝买，一元七个。
建议买几十个，微博限制的严，太频繁了会出现302转移。
或者你也可以把时间间隔调大点。
"""
myWeiBo = [
    {'no': 'xxxxxxxxx', 'psw': 'xxxxxxxxx'},
    # {'no': 'shudieful3618@163.com', 'psw': 'a123456'},
]

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")

def getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    for elem in weibo:
        account = elem['no']
        password = elem['psw']
        username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": username,
            "service": "sso",
            "sp": password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        session = requests.Session()
        r = session.post(loginURL, data=postData)
        print(r)
#     #     jsonStr = r.content.decode('gbk')
#     #     info = json.loads(jsonStr)
#     #     if info["retcode"] == "0":
#     #         print("Get Cookie Success!( Account:%s )" % account)
#     #         cookie = session.cookies.get_dict()
#     #         cookies.append(cookie)
#     #     else:
#     #         print("Failed!( Reason:%s )" % info['reason'])
#     # return cookies
#
#
# cookies = getCookies(myWeiBo)
# print ("Get Cookies Finish!( Num:%d)" % len(cookies))




# if __name == '__main__':
