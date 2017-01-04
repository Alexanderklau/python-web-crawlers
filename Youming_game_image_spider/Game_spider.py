import requests
from bs4 import BeautifulSoup
import time
import re

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.5',}
for i in range(1,10):
    url = 'http://down.gamersky.com/page/pc/0-0-0-0-0-0-0-00_' + str(i) +  '.html'
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('div.tit')
    date = soup.find_all(text=re.compile(u'更新日期'))
    language = soup.find_all(text=re.compile(u'游戏类型'))
    for title,date,language in zip(title,date,language):
        data = {
            'title':title.get_text(),
            'date':date
        }
        print(data)


