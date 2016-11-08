from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "http://www.mmkao.net/wcgz/"
html = urlopen(url)
bsObj = BeautifulSoup(html)
for link in bsObj.find("div",{"style":"background-image:url(../Image2/left_box_bg.gif);"}).findAll(
    "a",href = re.compile("^([0-9])")):
    if 'href' in link.attrs:
        realUrl = url + link.attrs['href']
        f = open('myfile','w')
        c = f.write(realUrl)
        #print(link.attrs['href'])
        #realUrl = "http://www.mmkao.net/wcgz/" + link.attrs['href']
        print(realUrl)

