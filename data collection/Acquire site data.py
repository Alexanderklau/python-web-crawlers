from urllib.request import urlopen
from bs4 import  BeautifulSoup
import re
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").finaAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("As if this site lack data.But don't worry!")

        for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    newPage = link.attrs['href']
                    print("----------------\n"+newPage)
                    pages.add(newPage)
                    getLinks(newPage)
    getLinks("")
