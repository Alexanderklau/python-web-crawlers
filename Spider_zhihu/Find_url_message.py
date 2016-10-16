from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    html = urlopen("https://www.zhihu.com" + pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.find(id = "zh-question-list"))
    except AttributeError:
        print("This pages not have property,Dont worry!")

    for link in bsObj.findAll("a",href=re.compile("^(/question/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print("----------\n"+newpage)
                pages.add(newpage)
                getLinks(newpage)
getLinks("")