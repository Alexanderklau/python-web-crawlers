from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.mmkao.net/")
bsobj = BeautifulSoup(html)
print(bsobj.find())