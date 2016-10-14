from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("https://movie.douban.com/chart" + pageUrl)
    bsObj = BeautifulSoup(html)
    print(bsObj.h1.get_text())
    print(bsObj.find(id="content").findAll("tbody")[0])
    print(bsObj.find(id="douban-top250").find("span").find("a").attrs['href'])
