# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://www.baidu.com/'
html = urlopen(url)
bsobj = BeautifulSoup(html.read())
print(bsobj.title)