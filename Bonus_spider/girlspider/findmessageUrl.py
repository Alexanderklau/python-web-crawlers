from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.mmkao.net/")

bsobj = BeautifulSoup(html)

girlname = bsobj.findAll("ul",{"class":"photo"})
for name in girlname:
    print(len(name.get_text()))
