#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import time

url = 'http://pic.ali213.net/list/game/'
urls = ['http://pic.ali213.net/list/game/index_{}.html'.format(str(i)) for i in range(2,10)]
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
}

def get_attracations(url,data=None):
    wb_data = requests.get(url,headers=headers)
    wb_data.encoding = 'utf-8'
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('li.box > em')
    image = soup.select('img')
    href = soup.select('li.box > a')    
    print(href)
    for title, image,href in zip(title, image,href):
        data = {
            'title': title.get_text(),
            'image': image.get('src'),
            'href' : href.get('href'),
        }
        print(data)
for single_urls in urls:
    get_attracations(single_urls)


