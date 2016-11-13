from urllib.request import urlretrieve,urlopen
from bs4 import BeautifulSoup
import re

url = "http://www.3dmgame.com/gl/?tid=26&totalpage=527&page=1"
html = urlopen(url)
bsObj = BeautifulSoup(html)
for link in bsObj.find("div",{"class":"QZlisttxt"}).findAll("a",href=re.compile("()")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
