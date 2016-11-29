#-*-coding:utf-8-*-
from urllib.request import urlopen,urlretrieve,Request
from bs4 import BeautifulSoup
import re
import urllib.response


page = 1
for i in range(1,1000):
    page = i
    url = 'http://www.jiu-tuo.com/list-jiutuo--' + str(page)
    req = Request(url,headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Referer': url,
        'Host':'www.jiu-tuo.com'})
    html = urlopen(req)
    bsObj = BeautifulSoup(html)
    name = bsObj.findAll("tr")
    print(name)


