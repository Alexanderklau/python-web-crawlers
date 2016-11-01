import os
from urllib.request import urlretrieve,urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.mmkao.net/Beautyleg/201610/12161.html")
bsObj = BeautifulSoup(html)
imageLoaction = bsObj.find("ul",{"class":"file"}).find("img")["src"]
urlretrieve(imageLoaction)