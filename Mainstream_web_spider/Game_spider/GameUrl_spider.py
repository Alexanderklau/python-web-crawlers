import requests
from bs4 import BeautifulSoup
import time
url = 'http://down.gamersky.com/pc/?sort=30&list='
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Host':'down.gamersky.com',}

def get_url_message(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('div.tit > a')
    star = soup.select('div.txt')
    for title,star in zip(title,star):
        data = {

            'star': star.get_text(),

        }
        print(data)

def get_more_pages(start,end):
    for one in range(start,end):
        get_url_message(url + str(one))
        time.sleep(2)
get_more_pages(1,20)
