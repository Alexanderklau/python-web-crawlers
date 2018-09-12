from urllib.request import urlretrieve,urlopen,Request
from bs4 import BeautifulSoup
import re


url = "http://www.mmkao.net/"
req = Request(url,headers = {'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'})
html = urlopen(req)
bsObj = BeautifulSoup(html)
for link in bsObj.find("li").findAll("a"):
    if 'href' in link.attrs:
        href = link.attrs['href']
        print(href)