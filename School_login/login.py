#-*-coding:utf-8-*-
from urllib.request import urlopen,urlretrieve,Request
from bs4 import BeautifulSoup

url = 'http://210.41.224.117/Login/xLogin/Login.asp'
req = Request(url,headers={
                  'Connection': 'Keep-Alive',
                  'Accept': 'text/html, application/xhtml+xml, */*',
                  'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                  'Host':'210.41.224.117',
                  'Referer':url,})
html = urlopen(req)
bsObj = BeautifulSoup(html)
print(bsObj)
