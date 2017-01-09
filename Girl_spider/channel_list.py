import requests
from bs4 import BeautifulSoup
start_urls = 'http://www.mmkao.net/'
def Find_urls(url):
    wb_data = requests.get(url)
    wb_data.encoding = 'gb2312'
    soup = BeautifulSoup(wb_data.text,"lxml")
    links = soup.select('div.dh > ul li a')
    for link in links:
        # imageUrl = 'http://www.mmkao.net/' + link.get('href')
        a = link.get('href')
        print(a)
        # print(imageUrl)

Url_list = """
http://www.mmkao.net/Beautyleg/
http://www.mmkao.net/RQ-STAR/
http://www.mmkao.net/ROSI/
http://www.mmkao.net/ligui/
http://www.mmkao.net/4K-Star/
http://www.mmkao.net/DISI/
http://www.mmkao.net/NAKED-ART/
http://www.mmkao.net/PANS/
http://www.mmkao.net/3Agirl/
"""
type_list = """
Beautyleg/
RQ-STAR/
ROSI/
ligui/
4K-Star/
DISI/
NAKED-ART/
PANS/
3Agirl/
"""
