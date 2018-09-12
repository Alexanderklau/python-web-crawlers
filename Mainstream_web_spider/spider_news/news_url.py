import requests
from bs4 import BeautifulSoup
import time
import re
from headers import headers
from proxy import proxies
def Text_spider(url):
    wb_data = requests.get(url,headers=headers,proxies=proxies)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('h3')
    print(title)


Text_spider('https://tieba.baidu.com/p/4619725452')
