from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://news.sina.com.cn")
bsObj = BeautifulSoup(html)

for child in bsObj.findAll("img",{"src":re.compile("\.\/slidenews/1_t5000/2016_42/65716_740165_423941.jpg ")})