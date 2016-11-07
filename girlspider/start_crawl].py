from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.mmkao.net/")
bsobj = BeautifulSoup(html)
for link in bsobj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])