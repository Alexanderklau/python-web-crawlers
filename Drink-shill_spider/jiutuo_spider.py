# -*-coding:utf-8 -*-
__author__ = 'Yemilice_lau'
import requests
from bs4 import BeautifulSoup
import re
url = 'http://tieba.baidu.com/f?kw=%E6%88%92%E8%B5%8C&ie=utf-8&pn=0'
html = requests.get(url)
# wb_data = BeautifulSoup(html.text,'lxml')
soup = html.text
# <a class="j_th_tit " target="_blank" title="实在没钱了，便宜处理过年朋友送" href="/p/4975871005" clicked="true">实在没钱了，便宜处理过年朋友送</a>
text = re.compile(r'<title>(.*?)</title>',re.VERBOSE)
title = re.search(text,soup).group(0)
print(title)









# if __name__ == '__main__':