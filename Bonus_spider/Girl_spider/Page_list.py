import requests
from bs4 import BeautifulSoup
import time
import re
import pymongo
import random
from urllib.request import urlopen
client = pymongo.MongoClient('localhost',27017)
Image = client['Image']
GirlID = Image['ID']
GirlUrl = Image['Url']
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
    wb_data.encoding = 'gb2312'
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('ul.photo > li a > img')
    for link in links:
        title = link.get('alt')
        ID = '\d'
        tx = re.findall(ID, title)
        str1 = ""
        str1 = str1.join(tx)
        if len(str1) >= 4:
            a = str1[0]
            b = str1[1]
            c = str1[2]
            if a == '0' and b == '0' and c == '0':
                d = str1.replace(c, ' ')
                print(d.split())
            elif a == '0' and b == '0':
                d = str1.replace(b, ' ')
                print(d.split())
            elif a == '0':
                d = str1.replace(a, ' ')
                print(d.split())
            else:
                print(str1)
        elif len(str1) == 3:
            a = str1[0]
            b = str1[1]
            if a == '0' and b == '0':
                d = str1.replace(b,' ')
                print(d.split())
            elif a == '0':
                d = str1.replace(a,' ')
                print(d.split())
            else:
                print(str1)
        else:
            print(str1)

        # if str1[0] == '0':
        #     str2 = str1.strip('0')
        #     GirlID.insert_one({'ID': str2})
        # else:
        #     GirlID.insert_one({'ID': str1})