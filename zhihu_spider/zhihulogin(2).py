# -*- coding: UTF-8 -*-
import urllib
from bs4 import BeautifulSoup
import urllib2
import cookielib
import time

class ZhihuLogin(object):
    def __init__(self,url):
        self.header = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.26\
            23.87 Safari/537.36',}
        self.login_url = url
        self.data = None
        self.opener = None
        self.cookies = None
        self.account = None
        self.password = None

    def First_login(self,account,password):
        self.account = account
        self.password = password
        self.data = {
            'email_num' : self.account,
            'password' : self.password,
            'remember_me':'true'}
        try:
            captcha = self.get_captcha()
            self.data['captcha'] = captcha
        except:
            print 'no captcha'

        self.use_cookies()
        self.opener = self.get_opener()
        data = urllib.urlencode(self.data)
        request = urllib2.Request(self.login_url,data,self.header)
        self.opener.open(request)
        self.cookies.save(ignore_discard = True,ignore_expires = True)

    def use_cookies(self):
        filename = 'cookies.txt'

        try:
            cookies = cookielib.MozillaCookieJar()
            cookies.load(filename)
            isLogin = True
            self.cookies = cookies
        except:
            print "cookies load fail"
            isLogin = False
            self.cookies = cookielib.MozillaCookieJar(filename)

        return isLogin

    def get_opener(self):
        handler = urllib2.HTTPCookieProcessor(self.cookies)
        opener = urllib2.build_opener(handler)
        return opener

    def get_data(self):#检查是否登陆

        url_judge = "https://www.zhihu.com/settings/profile"
        isLogin = True
        if self.opener == None:
            isLogin = self.use_cookies()
            self.opener = self.get_opener()

        if isLogin == False:
            return False

        html = self.opener.open(url_judge).read()

        soup = BeautifulSoup(html,'html.parser')
        node = soup.find("span",class_="name")
        print node.get_text()

    def get_captcha(self):

        t = str(int(time.time() * 1000))
        captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
        html = urllib2.urlopen(captcha_url).read()

        fout = open("captcha.jpg","wb")
        fout.write(html)
        fout.close()

        chptcha = raw_input("input the captcha: ")
        return chptcha

if __name__=="__main__":
    url = "http://www.zhihu.com/login/email"
    zhihu = ZhihuLogin(url)
    while zhihu.get_data() == False:
        account = raw_input("input the email: ")
        password = raw_input("input the password: ")
        zhihu.First_login(account,password)




