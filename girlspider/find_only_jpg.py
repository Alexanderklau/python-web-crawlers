from urllib.request import urlretrieve,urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.mmkao.net/Sityle/")
bsobj = BeautifulSoup(html)
image = bsobj.find("img")["src"]
print(image)