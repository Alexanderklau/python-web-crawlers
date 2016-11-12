from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

html = urlopen("http://www.3dmgame.com/gl/201611/3607033.html")
bsObj = BeautifulSoup(html)
content = bsObj.find("div",{"class":"con"})
print(content.get_text())
