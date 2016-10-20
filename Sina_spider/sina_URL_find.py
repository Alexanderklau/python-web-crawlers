from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.sina.com.cn")
bsObj = BeautifulSoup(html)
for link in bsObj.find("div",{"id":""})