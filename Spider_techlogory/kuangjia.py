# -*-coding:utf-8 -*-
__author__ = 'Yemilice_lau'
import requests
from bs4 import BeautifulSoup
import re
def get_links(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    Bsobj = BeautifulSoup(html.text,'lxml')
    title = re.findall('a class="slideNewsLeft" \d>(\d)</a>',Bsobj)
    print(title)


def links_crawler():
    pass

get_links('http://www.sina.com.cn/')








# if __name__ == '__main__':