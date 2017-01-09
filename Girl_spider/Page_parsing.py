import requests
from bs4 import BeautifulSoup
import time
import re
import pymongo
import random
from urllib.request import urlopen
from channel_list import type_list,Url_list
client = pymongo.MongoClient('localhost',27017)
Girl = client['Girl']
GirlID = Girl['ID']
GirlUrl = Girl['Url']
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

def get_links_from(channel,pages):
    #http://www.mmkao.net/Beautyleg/2.html
    lise_view = '{}/{}.html'.format(channel,str(pages))
    wb_data = requests.get(lise_view,headers = headers,proxies = proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('ul.photo > li a')
    for link in links:
        pageUrl = link.get('href')
        print(pageUrl)
        # GirlUrl.insert_one({'url':pageUrl})
get_links_from('http://www.mmkao.net/Beautyleg/',3)
def get_item_info(url):
    wb_data = requests.get(url,headers = headers,proxies = proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('title')[0].text
    ID = '\d'
    tx = re.findall(ID, title)
    str1 = ""
    ID = str1.join(tx)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.select('title')[0].text
    np = '404' in title
    if np:
        pass
    else:
        ID = '\d'
        str1 = ""
        tx = re.findall(ID, title)
        str1 = str1.join(tx)
        if str1[0] == '0':
            str2 = str1.strip('0')
            GirlID.insert_one({'ID':str2})
        else:
            GirlID.insert_one({'ID':str1})
#http://img.mmkao.net/photo/beautyleg/beautyleg1334/27.jpg
def Download_Url(channel,num):
    list_view = '{}/{}.jpg'.format(channel,str(num))



# get_links_from('http://www.mmkao.net/Beautyleg/',2)