from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.mmkao.net/")
bsobj = BeautifulSoup(html)
images = bsobj.findAll("img")
for image in images:
    print(image["src"])