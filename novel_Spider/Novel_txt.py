#-*- coding:gbk -*-
from urllib.request import *
import re
from bs4 import BeautifulSoup

url = 'http://www.quanshu.net/'
req = urlopen(url)
bsObj = BeautifulSoup(req)
for i in bsObj.find("li").findAll("a",href=re.compile("(book)")):
    if 'href' in i.attrs:
        href = i.attrs['href']
        print(href)


