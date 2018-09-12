# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
import re
url = 'http://jandan.net/ooxx/page-2328#comments'
html = requests.get(url)
extect = html.text
# <a class="view_img_link" target="_blank" href="//wx3.sinaimg.cn/large/68f6e545ly1fc6lm1e6a5g20cs076he3.gif">
imageUrl = set(re.findall('img\ssrc="(.*?)"',extect,re.S))
# print(imageUrl)
print(imageUrl)