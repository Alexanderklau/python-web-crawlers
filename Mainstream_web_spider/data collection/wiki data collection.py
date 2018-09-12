from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/China")
#Make use of BeatifulSoup analysis HTML data
bsobj = BeautifulSoup(html)
#Find "a" header URL
for link in bsobj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
