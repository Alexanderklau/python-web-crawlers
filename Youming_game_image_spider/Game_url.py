from urllib.request import urlretrieve,urlopen,Request
from bs4 import BeautifulSoup
import re
page = 9
url = "http://pic.ali213.net/list/tagList/4_%d.html" %(page)
req = Request(url,headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
html = urlopen(url)
bsObj = BeautifulSoup(html)
for link in bsObj.find("em").findAll("a"):
    if 'href' in link.attrs:
        href = link.attrs['href']
        print(href)

