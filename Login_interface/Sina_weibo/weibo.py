# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
from bs4 import BeautifulSoup
from lxml import etree
from multiprocessing.dummy import Pool
cook = {'Cookie':"SCF=AvIj3yrfnwmJSAXz4ENJsho6C_7O8YU4aNH2g7ezF7WH9K2VbS8zpqN4B_-HtlwDio4UCqdksk9wC_6L2kU40Gk.; expires=Tue, 02 Feb 2027 13:07:31 GMT; path=/; domain=.sina.cn; HttpOnly"}
url = 'http://weibo.cn/?tf=5_009&vt=4'
# html = requests.get(url).content
# print(html)
html = requests.get(url,cookies = cook).content
bsobj = BeautifulSoup(html)
print(bsobj)
# https://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=4






# if __name == '__main__':