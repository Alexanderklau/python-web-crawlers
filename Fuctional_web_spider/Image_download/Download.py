#-*- coding:utf-8 -*-
import re
import urllib
from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup


def getHtml(url):
    page = urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        urlretrieve(imgurl, '%s.jpg' % x)
        x = x + 1


html = getHtml("http://pic.yesky.com/c/6_20498_1.shtml")
getImg(html)