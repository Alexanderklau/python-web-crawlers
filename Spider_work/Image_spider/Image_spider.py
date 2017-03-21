# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
import time
import re
from bs4 import BeautifulSoup
from route_headres import headres
from route_IP import proxy_ip
from lxml import etree
import pymongo
client = pymongo.MongoClient('localhost',27017)
Ceshi = client['Image']
Page_list = Ceshi['Page_list']
Image_list = Ceshi['Image_list']
def href_list(channel,list):
    html = requests.get(channel, headers=headres, proxies=proxy_ip)
    selector = etree.HTML(html.text)
    pages = selector.xpath('//div[@class="sxye"]/ul/li[14]/a/@href')
    s = []
    for page in pages:
        x = page.split('_')[2][:-5]
        c1 = [x for x in range(1,int(x) + 1)]
        for c in c1:
            html = list + str(c) + '.html'
            s.append(html)
            # print(html)
    return s
def get_page(url):
    html = requests.get(url,headers = headres,proxies = proxy_ip)
    selector = etree.HTML(html.text)
    time.sleep(2)
    page_urls = selector.xpath('//ul[@class="u8"]/li/a[@class="title"]/@href')
    for page_url in page_urls:
        Page_list.insert_one({'page_list':page_url})
        return page_url
def get_Image(url):
    html = requests.get(url)
    time.sleep(2)
    html.encoding = 'gb2312'
    soup = BeautifulSoup(html.text,'lxml')
    if soup.find_all('li','thisclass'):
        Sum_page = soup.select('div.dede_pages li')[0].text
        pages = re.search('共(\d)页',Sum_page).group(1)
        for page in range(2,int(pages)):
            page_url = url[:-5] + '_' + str(page) + '.html'
            htmls = requests.get(page_url)
            Image = BeautifulSoup(htmls.text,'lxml')
            Image_Urls = Image.select('div.page-list img.src')
            for Image_Url in Image_Urls:
                Image_list.insert_one({'Image_list',Image_Url.get('src')})
    else:
        Image_Urls = soup.select('div.page-list img')
        for Image_Url in Image_Urls:
            Image_list.insert_one({'Image_list', Image_Url.get('src')})
