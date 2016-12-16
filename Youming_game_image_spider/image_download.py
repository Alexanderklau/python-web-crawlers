from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import *
import re
import time

def Find_url():
    url = 'http://tu.3dmgame.com/beauty/'
    req = Request(url,headers={'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',})
    bsObj = urlopen(req)
    html = BeautifulSoup(bsObj)
    return html
def ImgeUrl():
    ImageUrl = Find_url().find("div",{"id":"container"}).findAll("a",href=re.compile("^(http://)"))
    for link in ImageUrl:
        if 'href' in link.attrs:
            href = link.attrs['href']
            

print(ImgeUrl())
