from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

url = "http://www.3dmgame.com/gl/"

def name(url):
    page = 1
    url = "http://www.3dmgame.com/gl/?tid=26&totalpage=527&page=" + str(page)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    title = bsObj.find("div",{"class":"QZlisttxt"}).findAll("p")

def Url(url):
    page = 1
    url = "http://www.3dmgame.com/gl/?tid=26&totalpage=527&page=" + str(page)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    for link in bsObj.find("div", {"class": "QZlisttxt"}).findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])


