# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import threading
import time
import random
import requests
from lxml import etree
import re
# url = 'http://www.mmkao.net/Beautyleg/'
def list_url(url):
    html = requests.get(url)
    Selector = etree.HTML(html.text)
    end_page = str(Selector.xpath('//ul[@class="page"]/a[4]/@href'))[2:-7]
    print('The atlas has %s page'%end_page)
    for i in range(2,int(end_page) + 1):
        next_url = url + str(i) + '.html'
        return next_url
def Image_url(url):
    html = requests.get(url)
    Selector = etree.HTML(html.text)
    image = Selector.xpath('//ul[@class="photo"]/li/a/@href')
    for i in image:
        pageUrl = 'http://www.mmkao.net/Beautyleg/' + i
        return pageUrl
# def download_image(url):
#     html = requests.get(url)
#     Selector = etree.HTML(html.text)
#     end_image_page = str(Selector.xpath('//ul[@class="image"]/strong[1]/text()'))[2:-2]
#     print('The image_page have %s page'%end_image_page)
#
#
# download_image('http://www.mmkao.net/Beautyleg/201612/12449.html')








# if __name == '__main__':