# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
import re
from lxml import etree
import pymongo
from route_ip import proxy_ip
from route_heanders import headers
client = pymongo.MongoClient('localhost',27017)
TM = client['TM']
TM_url = TM['TM_urls']
TM_info = TM['TM_info']

def Goods_message(url):
    html = requests.get(url,headers = headers,proxies = proxy_ip)
    selector = etree.HTML(html.text)
    prices = selector.xpath('//p[@class="productPrice"]/em/@title')
    names = selector.xpath('//div[@class="productTitle productTitle-spu"]/a[1]/text()')
    types = selector.xpath('//div[@class="productTitle productTitle-spu"]/a[2]/text()')
    companys = selector.xpath('//div[@class="productShop"]/a/text()')
    values = selector.xpath('//p[@class="productStatus"]/span[1]/em/text()')
    for price,name,type,company,value in zip(prices,names,types,companys,values):
        data = {
            '商品价格':price[:-3] + '元',
            '商品名称':name,
            '商品特点':type,
            '商品店铺':company.strip('\n'),
            '商品销量':value
        }
        TM_info.insert_one(data)
def get_goodsUrl():
    for i in range(1,101):
        url = "https://list.tmall.com/search_product.htm?type=pc&q=%CA%D6%BB%FA&totalPage=" + str(i) + "&sort=s&style=g&jumpto=100"
        TM_url.insert_one({'Url':url})



