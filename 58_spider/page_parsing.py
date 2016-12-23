# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
Ceshi = client['ceshi']
url_list = Ceshi['Url_list3']
item_info = Ceshi['Item_info3']

def get_links_from(channel,pages):
    #cd.58.com/danche/pn2/
    list_view = '{}/pn{}'.format(channel,str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):
        for link in soup.select('td.t > a.t'):
            item_link = link.get('href').split('?')[0]
            #url_list.insert_one({'url':item_link})
            print(item_link)
    else:
        pass
get_links_from('http://cd.58.com/danche/',2)

def get_item_info(url):
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('h1.info_titile')[0].text
    price = soup.select('span.price_now')[0].text
    area = list(soup.select('div.palce_li')[0].stripped_strings) if soup.find_all('div','palce_li') else None
    item_info.insert_one({'title':title,'price':price,'area':area})







