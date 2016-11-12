from urllib.request import urlopen
from bs4 import BeautifulSoup

page = 1
url = "http://www.3dmgame.com/gl/?tid=26&totalpage=527&page=" + str(page)
html = urlopen(url)
bsObj = BeautifulSoup(html)
title = bsObj.find("div",{"class":"QZlisttxt"}).findAll("p")
for name in title:
    txt = name.get_text()
    csvfile = open("page.txt","a+")
    csvfile.writelines(txt+'\n')
    csvfile.close()
