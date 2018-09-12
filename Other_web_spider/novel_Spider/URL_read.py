from urllib.request import *
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    for page in range(0, 11):
        page += 1
        url = 'http://www.quanshu.net/list/%d_1.html' % page
        req = Request(url, headers={
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        })
        html = urlopen(req)
        bsobj = BeautifulSoup(html)
        for i in bsobj.find("span", {"class": "l"}).findAll("a", href=re.compile("(book_\d)")):
            if 'href' in i.attrs:
                if i.attrs['href'] not in pages:
                    newPage = i.attrs['href']
                    print(newPage)
                    pages.add(newPage)
                    getLinks(newPage)

getLinks("")

