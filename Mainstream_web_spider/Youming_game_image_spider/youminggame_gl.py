from urllib.request import urlopen
from bs4 import BeautifulSoup

page = 1
url = "http://www.3dmgame.com/gl/?tid=26&totalpage=527&page=" + str(page)
html = urlopen(url)
bsObj = BeautifulSoup(html)

title = bsObj.find("div",{"class":"QZlisttxt"}).findAll("p")
for name in title:
    content = name.get_text()

for link in bsObj.find("div",{"class":"QZlisttxt"}).findAll("a"):
    if 'href' in link.attrs:
        REQ = link.attrs['href']
