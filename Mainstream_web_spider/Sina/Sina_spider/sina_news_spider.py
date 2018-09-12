from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://news.sina.com.cn/china/xlxw/2016-10-19/doc-ifxwvpar8492757.shtml")
bsObj = BeautifulSoup(html)
news = bsObj.findAll("div",{"class":"artical-player-wrap"})
for new in news:
    print(new.get_text())
