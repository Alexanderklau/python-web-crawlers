from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
import math

temp = 0
for x in range(1,20):
    temp += x
    url = "http://www.3dmgame.com/gl/?tid=26&totalpage=527&page=" + str(temp)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    for link in bsObj.find("div", {"class": "QZlisttxt"}).findAll("a"):
        if 'href' in link.attrs:
            txt = link.attrs['href']
            titleFile = open("title.txt","a+")
            titleFile.writelines(txt + '\n')



