# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import re
import requests
from multiprocessing import Pool
from lxml import etree
from bs4 import BeautifulSoup
header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Host':'www.xicidaili.com'
}
def ip_Spider(url):
    wb_data = requests.get(url,headers=header)
    html = BeautifulSoup(wb_data.text,'lxml')
    address = re.search('')









if __name__ == '__main__':
    ip_Spider('http://www.xicidaili.com/nn/1')