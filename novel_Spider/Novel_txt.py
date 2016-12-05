#-*- coding:gbk -*-
from urllib.request import *
import re
from bs4 import BeautifulSoup
import time

url = 'http://www.quanshu.net/'
req = urlopen(url)
bsObj = BeautifulSoup(req)
for i in bsObj.findAll("a",href=re.compile("(book_\d)")):
    if 'href' in i.attrs:
        href = i.attrs['href']
        txtUrl = urlopen(href)
        UrlObj = BeautifulSoup(txtUrl)
        for x in UrlObj.findAll("a",href=re.compile("(/book/\d/\d)$")):
            if 'href' in x.attrs:
                urlef = x.attrs['href']
                print(urlef)
                txt =open("url.txt","a+").writelines(urlef + '\n')



