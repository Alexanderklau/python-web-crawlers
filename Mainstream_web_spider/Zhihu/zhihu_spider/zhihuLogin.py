# -*- coding:utf -8 -*-
import requests
import http.cookiejar
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass

agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
headers = {
    "Host":"www.zhihu.com",
    "Referer":"https://www.zhihu.com/",
    "User-Agent": agent
}
session = requests.session()
session.cookies = http.cookiejar.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_doscard=True)
except:
    print("Cookie 无法加载")

def get_xsrf():
    index_url = 'www.zhihu.com'
    index_page = session.get(index_url,headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    _xsrf = re.findall(pattern,html)
    return _xsrf[0]

def get_captcha():
    x = str(int(time.time() * 1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + x + "&type=login"
    r = session.get(captcha_url,headers=headers)
    with open('captcha.jpg','wb') as f:
        f.write(r.content)
        f.close()
    captcha = input("Please input the captcha")
    return captcha

def isLogin():
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False

def login(secret, account):
    # 通过输入的用户名判断是否是手机号
    if re.match(r"^1\d{10}$", account):
        print("手机号登录 \n")
        post_url = 'http://www.zhihu.com/login/phone_num'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': secret,
            'remember_me': 'true',
            'phone_num': account,
        }
    else:
        if "@" in account:
            print("邮箱登录 \n")
        else:
            print("你的账号输入有问题，请重新登录")
            return 0
        post_url = 'http://www.zhihu.com/login/email'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': secret,
            'remember_me': 'true',
            'email': account,
        }
    try:
        # 不需要验证码直接登录成功
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = login_page.text
        print(login_page.status_code)
        print(login_code)
    except:
        # 需要输入验证码后才能登录成功
        postdata["captcha"] = get_captcha()
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = eval(login_page.text)
        print(login_code['msg'])
    session.cookies.save()

try:
    input = input
except:
    pass


if __name__ == '__main__':
    if isLogin():
        print('您已经登录')
    else:
        account = input('请输入你的用户名\n>  ')
        secret = input("请输入你的密码\n>  ")
        login(secret, account)

