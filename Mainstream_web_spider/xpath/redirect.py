# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import re

import requests

url = 'https://www.baidu.com/'
html = requests.get(url)
html.encoding = 'utf-8'
des = html.text
# title = re.findall('<title>(.*?)</title>',des,re.S)
title = re.search('<title>(.*?)</title>',des).group(1)
print(title)


