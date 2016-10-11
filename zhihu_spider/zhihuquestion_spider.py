from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("https://www.zhihu.com" + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div",{"id":"zh-profile-activity-page-list"}).findAll("a",href=re.compile("^(/question/)((?!:).)*$"))
links = getLinks("/people/yemilice")
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
