__author__ = 'CQC'


from urllib.request import urlopen,urlretrieve,build_opener,Request,HTTPCookieProcessor
from urllib.parse import urlencode
import http.cookiejar
import re

class SDU:
    def __init__(self):
        self.loginUrl = '****************'
        self.cookies = http.cookiejar.CookieJar()
        self.postdata = urlencode({
            "txtId":"*********",
            "txtMM":"*&******"
        }).encode(encoding='gbk')
        self.opener = build_opener(HTTPCookieProcessor(self.cookies))

    def getPage(self):
        requeset = Request(
            url = self.loginUrl,
            data= self.postdata)
        result = self.opener.open(requeset)

        print(result.read().decode('utf-8'))

sdu = SDU()
sdu.getPage()
