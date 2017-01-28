# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from lxml import etree
import requests
import json

url = 'http://www.163.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.5'
}
html = requests.get(url,headers=headers)
selector = etree.HTML(html.text)
title = selector.xpath('//title/text()')