import requests
from bs4 import BeautifulSoup
import time
import re
url = 'http://zhuanzhuan.58.com/detail/810842535537672199z.shtml'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
title = soup.title.text
print(title)
price = soup.select('span.price_now')
area = soup.select('div.palce_li > span')

data = {
    'price':price[0].text,
    'area' :area[0].text,
    'title':title
}
print(data)