from bs4 import BeautifulSoup
import re
import json
import time
import requests
from urllib.request import urlopen
for i in range(1,11):
    wb_date = requests.get('http://down.gamersky.com/page/pc/0-0-0-0-0-0-0-00_' + str(i) + '.html')
    soup = BeautifulSoup(wb_date.text,'lxml')
    for ID in soup.findAll("div",{"class":"txt ratingdownmore"}):
        if 'data-generalid' in ID.attrs:
            GameID = ID.attrs['data-generalid']
            url = 'http://i.gamersky.com/apirating/init?callback=jQuery&generalId=' + str(GameID)
            wb_data = urlopen(url).read().decode()
            s = wb_data[7:-2]
            js = json.loads(str(s))
            print(js['Average'])
    # GameID = ID.get('data-generalid')
    # print(GameID)



