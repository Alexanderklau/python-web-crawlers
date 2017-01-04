# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import pymongo
import re
client = pymongo.MongoClient('localhost',27017)
Ceshi = client['ceshi']
url_list = Ceshi['Url_list3']
item_info = Ceshi['Item_info3']
page = set()
def get_links_from(channel,pages):
    global page
    #cd.58.com/danche/pn2/
    list_view = '{}/pn{}'.format(channel,str(pages))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.findAll("a",href=re.compile('zhuanzhuan*')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in page:
                newPage = link.attrs['href'].split('?')[0]
                print(newPage)
                page.add(newPage)
                url_list.insert_one({'url':newPage})
                # get_links_from(channel,newPage)
# get_links_from('http://cd.58.com/diannao/',2)

def get_item_info(url):
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(1)
    title = soup.select('h1.info_titile')[0].text
    print(type(title))
    price = soup.select('span.price_now')[0].text if soup.find_all('span','price_now') else None
    # area = list(map(lambda x:x.text,soup.select('div.palce_li > span > i'))),
    area = list(soup.select('div.palce_li > span > i')[0].stripped_strings) if soup.find_all('div','palce_li') else None
    # item_info.insert_one({'title':title,'price':price,'area':area,'url':url})
    print({'title':title,'price':price,'area':area,'url':url})

get_item_info('http://zhuanzhuan.58.com/detail/813641600154550276z.shtml')



