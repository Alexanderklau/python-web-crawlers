# -*- coding: utf-8 -*-
from urllib.request import HTTPCookieProcessor,\
    build_opener,install_opener,HTTPHandler,urlopen,quote,Request
from urllib.parse import urlencode
import http.cookiejar
import sys
import rsa
import binascii
import json
import base64
import re

class Weibo_login:
    def enableCookie(self):
        cj = http.cookiejar.CookieJar()
        cookie_support = HTTPCookieProcessor(cj)
        opener = build_opener(cookie_support,HTTPHandler)
        install_opener(opener)

    def getServerData(self):
        url = 'https://login.sina.com.cn/sso/prelogin.php?\
        entry=weibo&callback=sinaSSOController.preloginCallBack&\
        su=NDI5MDk1ODE2JTQwcXEuY29t&rsakt=mod&checkpin=1&client\
        =ssologin.js(v1.4.18)&_=1477215123499'
        data = urlopen(url).read()
        p = re.compile('(.*)')
        try:
            json_data = p.search(data).group(1)
            data = json.loads(json_data)
            servertime = str(data['servertime'])
            nonce = data['nonce']
            pubkey = data['pubkey']
            rsakey = data['rsakv']
            return servertime,nonce,pubkey,rsakey
        except:
            print("Get servertime error")
            return None

    def getPassword(self, password, servertime, nonce, pubkey):
        rsaPublickey = int(pubkey, 16)
        key = rsa.PublicKey(rsaPublickey, 65537)
        message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)  # 拼接明文js加密文件中得到
        passwd = rsa.encrypt(message, key)
        passwd = binascii.b2a_hex(passwd)
        return passwd


    def getUsername(self, username):
        username_ = quote(username)
        username = base64.encodestring(username_)[:-1]
        return username

    def getFormData(self, userName, password, servertime, nonce, pubkey, rsakv):
        userName = self.getUsername(userName)
        psw = self.getPassword(password, servertime, nonce, pubkey)

        form_data = {
            'entry': 'weibo',
            'gateway': '1',
            'from': '',
            'savestate': '7',
            'useticket': '1',
            'pagerefer': 'http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=ht\
            tp%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F',
            'vsnf': '1',
            'su': 'NDI5MDk1ODE2JTQwcXEuY29t',
            'service': 'miniblog',
            'servertime': '1477215141',
            'nonce': 'J2QL7N',
            'pwencode': 'rsa2',
            'rsakv': '1330428213',
            'sp': 'd72a330ae92b0bf1ebea34f7255ac2f9865ea52537509\
            b243524c08a55a71efcc41e1386809c65f8402c30c9ee3895328b\
            d38068004734162994109d928957fd87c35051f7b3f1e8e3f9ff66\
            6ed9dd857d07c1a7aebe86c3db01da5302815a2fc100af76206ee5\
            6ce1f3d21dc30cc5338e14d43c36ccf62f19f3bb024186395f',
            'sr': '1376*774',
            'encoding': 'UTF-8',
            'prelt': '89',
            'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype': 'META'
        }
        formData = urlencode(form_data)
        return formData

        # 登陆函数

    def login(self, username, psw):
        self.enableCookies()
        url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
        servertime, nonce, pubkey, rsakv = self.getServerData()
        formData = self.getFormData(username, psw, servertime, nonce, pubkey, rsakv)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'}
        req = Request(
            url=url,
            data=formData,
            headers=headers
        )
        result = urlopen(req)
        text = result.read()
        print
        text
        # 还没完！！！这边有一个重定位网址，包含在脚本中，获取到之后才能真正地登陆
        p = re.compile('location\.replace[\'"](.*?)[\'"]')
        try:
            login_url = p.search(text).group(1)
            print
            login_url
            # 由于之前的绑定，cookies信息会直接写入
            urlopen(login_url)
            print
            "Login success!"
        except:
            print
            'Login error!'
            return 0

            # 访问主页，把主页写入到文件中
        url = 'http://weibo.com/u/2679342531/home?topnav=1&wvr=6'
        request = Request(url)
        response = urlopen(request)
        text = response.read()
        fp_raw = open("e://weibo.html", "w+")
        fp_raw.write(text)
        fp_raw.close()
        # print text


wblogin = Weibo_login()
print
'新浪微博模拟登陆:'
username = input(u'用户名：')
password = input(u'密码：')
wblogin.login(username, password)


