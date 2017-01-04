from bs4 import BeautifulSoup
import re
import json
import time
import requests
from urllib.request import urlopen
import pymongo
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.5',}
for i in range(1,12):
    wb_date = requests.get('http://down.gamersky.com/page/pc/0-0-0-0-0-0-0-00_' + str(i) + '.html',headers=headers)
    soup = BeautifulSoup(wb_date.text,'lxml')
    title = soup.select('div.tit')
    date = soup.find_all(text=re.compile(u'更新日期'))
    ID = soup.select('div.ratingdownmore')
    language = soup.find_all(text=re.compile(u'游戏类型'))
    # print(ID)
    for title, date, language,ID in zip(title, date, language,ID):
        data = {
            'title': title.get_text(),
            'date': date,
            'type':language,
            'ID':ID.get('data-generalid')
        }
        # print(data)
        # for ID in soup.findAll("div",{"class":"txt ratingdownmore"}):
        #     if 'data-generalid' in ID.attrs:
        #         GameID = ID.attrs['data-generalid']
        url = 'http://i.gamersky.com/apirating/init?callback=jQuery&generalId=' + str(data['ID'])
        wb_data = urlopen(url).read().decode()
        s = wb_data[7:-2]
        js = json.loads(str(s))
        star = js['Average']
        data['star'] = star
        time.sleep(3)
        print(data)








    # GameID = ID.get('data-generalid')
    # print(GameID)



