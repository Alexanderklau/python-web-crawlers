#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"}
all_url = 'http://www.mmkao.net/Sityle/'
start_html = requests.get(all_url,headers=headers)
Soup = BeautifulSoup(start_html.text,'lxml')
all_a = Soup.find('ul',class_='photo').find_all('a')
for a in all_a:
    title = a.get_text()
    href = a['href']
    print(title,href)
