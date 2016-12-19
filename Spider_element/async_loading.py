import requests
from bs4 import BeautifulSoup
import time

url =  'http://pic.ali213.net/list/star/index_'
taxt = '.html'
def get_page(url,data=None):
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('li.box > em')
    links = soup.select('li.box > a')
    for links,title in zip(links,title):
        data = {
            'links':links.get('href'),
            'title':title.get_text(),
        }
        print(data)
def get_more_page(start,end):
    for one in range(start,end):
        get_page(url + str(one) + taxt)
        time.sleep(2)

get_more_page(2,10)