from urllib.request import Request,urlopen,urlretrieve
from bs4 import BeautifulSoup
import re

url = 'https://book.douban.com/tag/%E6%8E%A8%E7%90%86?start=20'
req = Request(url,headers = {'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',})
html = urlopen(req)
bsObj = BeautifulSoup(html)
print(bsObj)
