import requests
from bs4 import BeautifulSoup
import pymongo
import time
import random

client = pymongo.MongoClient('localhost',27017)
Ganji = client['Ganji']
Url_list = Ganji['article_urls']
article_info = Ganji['article_info']

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.5'
}
proxy_list = [
    'http://222.169.193.162:8099',
    'http://171.38.154.86:8123',
    'http://60.176.164.2:8118',
    'http://180.104.106.130:8998',
]
proxy_ip = random.choice(proxy_list)
proxies = {'http:':proxy_ip}

def get_links(channel,pages,who_sells = 'o'):
    # http://cd.ganji.com/ershoubijibendiannao/o3/_macbook%20pro/
    list_view = '{}{}{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view,headers = headers,proxies = proxies)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('li','js-item'):
        for link in soup.select('li.js-item > a'):
            item_link = link.get('href').split('?')[0]
            Url_list.insert_one({'url':item_link})
            print(item_link)
    else:
        pass

def article_message(url):
    wb_data = requests.get(url,headers=headers,proxies=proxies)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    data = {
        'title':soup.select('h1.info_titile')[0].text,
        'price':soup.select('span.price_now')[0].text,
        'area':list(soup.select('div.palce_li')[0].stripped_strings) if soup.find_all('div','palce_li') else None,
        'crew':soup.select('p.personal_name')[0].text,
        'url':url
    }
    article_info.insert_one(data)
    print(data)

#article_message('http://zhuanzhuan.ganji.com/detail/809571294109646851z.shtml')








