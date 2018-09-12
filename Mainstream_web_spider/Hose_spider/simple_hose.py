import requests
from bs4 import BeautifulSoup
import time
import re
def house_spider(url):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('h3')
    price = soup.select('div.zu-side p')
    message = soup.select('div.zu-info p')[0].text

    print(message)
    area = soup.select('address.details-item')[0].text
    area = re.sub(' ','',area)
    area = re.sub('\n','',area)
    area = re.sub('］','',area)
    area = area.split('［')
    name = area[0]
    place = area[1]
    place = place.split('-')

house_spider('http://cd.zu.anjuke.com/fangyuan/p1/')