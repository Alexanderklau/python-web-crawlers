from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.mmkao.net/")
bsObk = BeautifulSoup(html)
for link in bsObk.findAll("img"):
    if 'src' in link.attrs:
        print(link.attrs['src'])