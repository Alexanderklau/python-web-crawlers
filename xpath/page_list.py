# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import re
import time
import requests
url = 'http://jandan.net/ooxx/page-1#comments'
total = 2328
for i in range(1,total+1):
    new_link = re.sub('page-\d','page-%d'%i,url,re.S)
    html = requests.get(new_link)
    Bsobj = html.text
    imageUrl = re.findall('img\ssrc="(.*?)"',Bsobj,re.S)
    for image in imageUrl:
        if 'http:' in image:
            print(image)
        else:
            print('http:' + image)
    # print(imageUrl)