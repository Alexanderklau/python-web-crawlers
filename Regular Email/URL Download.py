from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a",{"id":"logo"}).find("img")["src"]
urlretrieve(imageLocation,"logo.jpg")

