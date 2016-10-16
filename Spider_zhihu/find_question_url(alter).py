from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("https://www.zhihu.com" + articleUrl)
    bsObj = BeautifulSoup(html)
    return (bsObj.find("div", {"id": "zh-profile-answers-inner-list"}).findAll("a",href=re.compile("(/question/)((?!:).)*$")))
links = getLinks("/people/yemilice")
while len(links) > 0:
    newArticle = links[random.randint(0,len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

