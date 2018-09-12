# -*- coding: utf-8 -*-
'''
Required
- requests (必须)
- pillow (可选)
Info
- author : "xchaoinfo"
- email  : "xchaoinfo@qq.com"
- date   : "2016.2.4"
Update
- name   : "wangmengcn"
- email  : "eclipse_sv@163.com"
- date   : "2016.4.21"
'''
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass

headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Host':'210.41.224.117',
    'Referer':'http://210.41.224.117/Login/xLogin/Login.asp'}

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")

def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'http://210.41.224.117/Login/xLogin/yzmDvCode.asp?k=396225&t=' + t
    #'http://210.41.224.117/Login/xLogin/yzmDvCode.asp?k=396225&t=' + t
    r = session.get(captcha_url, headers=headers)
    with open('yzmDvCode.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('yzmDvCode.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到yzmDvCode.jpg 手动输入' % os.path.abspath('yzmDvCode.jpg'))
    captcha = input("please input the yzmDvCode\n>")
    return captcha


