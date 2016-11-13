#-*-coding:utf-8-*-
from urllib.request import urlretrieve,urlopen
from bs4 import BeautifulSoup
import re
import sys

temp = 0
for x in range(1,300):
    temp += x
    url = "http://www.3dmgame.com/gl/?tid=26&totalpage=527&page=" + str(temp)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    for link in bsObj.find("div",{"class":"QZlisttxt"}).findAll("a",href=re.compile("(/gl/)(\d)+")):
        if 'href' in link.attrs:
            href = link.attrs['href']
            content = urlopen(href)
            title = href[-12:]
            file = open(r'gl_txt/' + title,"wb").writelines(content)


        #http://www.3dmgame.com /gl/201611/3607132.html


