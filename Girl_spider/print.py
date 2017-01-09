import requests
from bs4 import BeautifulSoup
url = requests.get('http://www.mmkao.net/Beautyleg/201608/11681.html')
soup = BeautifulSoup(url.text,'lxml')
title = soup.select('title')[0].text
np = '404' in title
if np:
    pass
else:
    print('hello')