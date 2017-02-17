# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import re
import requests
from lxml import etree

header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Host':'www.xicidaili.com'
}
def ip_Spider(url):
    wb_data = requests.get(url,headers=header)
    selector = etree.HTML(wb_data.text)
    Address = selector.xpath('//table[@id="ip_list"]/tr/td[2]/text()')
    port = selector.xpath('//table[@id="ip_list"]/tr/td[3]/text()')
    locations = selector.xpath('//table[@id="ip_list"]/tr/td[4]/a/text()')
    for IP_address,IP_port,location in zip(Address,port,locations):
        data = {
            'Address':IP_address,
            'Port':IP_port,
            'Location':location
        }
        return data
# def Url_page():
#     url = 'http://www.xicidaili.com/nn/'
#     for i in range(1,100):
#         urls = url + str(i)
#         print(urls)









if __name__ == '__main__':
    ip_Spider('http://www.xicidaili.com/nn/1')