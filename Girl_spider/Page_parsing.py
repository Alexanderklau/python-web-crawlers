import requests
from bs4 import BeautifulSoup
import time
import re

def get_links_from(channel,pages):
    #http://www.mmkao.net/Beautyleg/2.html
    lise_view = '{}/{}.html'.format(channel,str(pages))
    wb_data = requests.get(lise_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('ul.photo > li a')
    for link in links:
        pageUrl = "http://www.mmkao.net/Beautyleg/" + link.get('href')
def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('title')[0].text
    ID = '\d'
    tx = re.findall(ID, title)
    str1 = ""
    ID = str1.join(tx)
    for i in range(1,41):
        if i < 10:
            x = ('0' + str(i))
            imageUrl = "http://img.mmkao.net/photo/beautyleg/beautyleg" + str(ID) + str(x) + ".jpg"
            print(imageUrl)
        else:
            imageUrl = "http://img.mmkao.net/photo/beautyleg/beautyleg" + str(ID) + str(i) + ".jpg"
            print(imageUrl)
# get_links_from('http://www.mmkao.net/Beautyleg/',2)
get_item_info('http://www.mmkao.net/Beautyleg/201611/12275.html')