# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from bs4 import BeautifulSoup
import re
import requests
def find_list():
    html = 'http://www.tu11.com/'
    bsobj = requests.get(html)
    bsobj.encoding = 'gb2312'
    Message = BeautifulSoup(bsobj.text,'lxml')
    hrefs = Message.select('div.header1 li a')
    for href in hrefs:
        x = 'http://www.tu11.com/' + href.get('href')


Url_list = """
    http://www.tu11.com//xingganmeinvxiezhen/list_1_1.html
    http://www.tu11.com//meituisiwatupian/list_2_1.html
    http://www.tu11.com//shenghuomeinvzipai/list_3_1.html
    http://www.tu11.com//qingchunmeinvxiezhen/list_4_1.html
    http://www.tu11.com//meinvtupianjingpin/list_5_1.html
    http://www.tu11.com//meinvxiezhenbizhi/list_9_1.html
    http://www.tu11.com//BEAUTYLEGtuimo/list_6_1.html
"""
Page_list = """
http://www.tu11.com//xingganmeinvxiezhen/list_1_
http://www.tu11.com//meituisiwatupian/list_2_
http://www.tu11.com//shenghuomeinvzipai/list_3_
http://www.tu11.com//qingchunmeinvxiezhen/list_4_
http://www.tu11.com//meinvtupianjingpin/list_5_
http://www.tu11.com//meinvxiezhenbizhi/list_9_
http://www.tu11.com//BEAUTYLEGtuimo/list_6_
"""







# if __name__ == '__main__':