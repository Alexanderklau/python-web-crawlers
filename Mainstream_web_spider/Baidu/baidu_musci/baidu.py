# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
import re
from bs4 import BeautifulSoup
url = 'http://music.baidu.com/top/dayhot'
wb_data = requests.get(url).content
print(wb_data)
# print(wb_data)








# if __name__ == '__main__':