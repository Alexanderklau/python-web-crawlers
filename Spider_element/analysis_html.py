#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests

url = 'http://pic.ali213.net/list/game/'
wb_data = requests.get(url)
wb_data.encoding = 'utf-8'
soup = BeautifulSoup(wb_data.text,'lxml')
title = soup.select('li.box > em')
print(type(title))
image = soup.select('img')
href = soup.select('li.box > a')
for title,image,href in zip(title,image,href):
    data = {
        'title' :title.get_text(),
        'image' :image.get('src'),
        'href'  :href.get('href'),
    }
    # print(data)
#print(soup)