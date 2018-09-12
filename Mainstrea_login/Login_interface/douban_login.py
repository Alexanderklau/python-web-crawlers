# -*- coding: utf-8 -*-
import requests
from html.parser import HTMLParser

class DoubanClient(object):
    def __init__(self,encoding='utf-8'):
        object.__init__(self)
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'origin':'http://www.douban.com'}
        self.session = requests.Session()
        self.session.headers.update(headers)
        self._encoding = encoding
    def Login(self,user,password,
              source = 'index_nav',
              redir = 'https://www.douban.com/',
              login = '登录',):
        url = 'https://accounts.douban.com/login'
        r = self.session.get(url)
        (captcha_id,captcha_url) = _get_Captcha(r.content)
        if captcha_id:
            captcha_solution = input('Please input solution for [%s]:' %captcha_url)
        data = {'form_email':user,
                'form_password':password,
                'source':source,
                'redir':redir,
                'login':login}
        if captcha_id:
            data['captcha-id'] = captcha_id
            data['captcha-solution'] = captcha_solution
        headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
                   'Host':'accounts.douban.com'}
        self.session.post(url,data=data,headers=headers)

def _attr(attrs, attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None

def _get_Captcha(content):
    class CaptchaParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.captcha_id = None
            self.captcha_Url = None

        def handle_starttag(self, tag, attrs):
            if tag == 'img' and _attr(attrs,'id') == 'captcha_image' and _attr(attrs,'class') == 'captcha_image':
                self.captcha_Url = _attr(attrs,'src')
            if tag == 'input' and _attr(attrs,'type') == 'hidden' and _attr(attrs,'name') == 'captcha-id':
                self.captcha_id == _attr(attrs,'values')
    p = CaptchaParser()
    p.feed(content)
    return p.captcha_id,p.captcha_Url



if __name__ == '__main__':
    c = DoubanClient()
    a = input('Enter username:')
    b = input('Enter password:')
    c.Login(a,b)
