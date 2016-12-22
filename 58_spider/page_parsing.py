# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
Ceshi = client['ceshi']
url_list = Ceshi['Url_list3']
item_info = Ceshi['Item_info3']

def get_links_from(channel,pages,who_sells=0):
    #cd.58.com/shouji/pn2/
    list_view = '{}{}/pn{}'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):
        for link in soup.select('td.t > a.t'):
            item_link = link.get('href').split('?')[0]
            # url_list.insert_one({'url':item_link})
            print(item_link)
    else:
        pass

def get_item_info(url):
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text,'lxml')
    not_loger_list = '404' in soup.find('script', type="text/javascript").get('src').split('/')
    if not_loger_list:
        pass
    else:
        title = soup.title.text
        price = soup.select('span.price.c_f50')[0].text
        date = soup.select('li.time')[0].text
        area = list(soup.select('span.c_25d > a[href^="/"]')[0].stripped_strings) if soup.find_all('span','c_25d') else None
        item_info.insert_one({'title':title,'price':price,'date':date,'area':area})
        print({'title':title,'price':price,'date':date,'area':area})









get_links_from('http://cd.58.com/shouji/',10)
