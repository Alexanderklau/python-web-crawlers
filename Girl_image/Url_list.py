# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from bs4 import BeautifulSoup
import requests
def find_url():
    url = 'http://mmkao.net/'
    html = requests.get(url)
    bsobj = BeautifulSoup(html.text,'lxml')
    Url_lists = bsobj.select('div.dh li a')
    # http://mmkao.net/RQ-STAR/
    for Url_list in Url_lists:
        page_url = 'http://mmkao.net/' + Url_list.get('href')
        print(page_url)
Url_list = """
http://mmkao.net/Beautyleg/
"""
# # http://mmkao.net/RQ-STAR/
# http://mmkao.net/TGOD/
# http://mmkao.net/ligui/
# http://mmkao.net/4K-Star/
# http://mmkao.net/DISI/
# http://mmkao.net/NAKED-ART/
# http://mmkao.net/PANS/
# http://mmkao.net/3Agirl/






# if __name__ == '__main__':