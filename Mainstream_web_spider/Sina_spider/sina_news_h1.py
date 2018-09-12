from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://news.sina.com.cn")
bsObj = BeautifulSoup(html.read())
print(bsObj.body)