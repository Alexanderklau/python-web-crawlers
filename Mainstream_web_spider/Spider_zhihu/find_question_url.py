from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.zhihu.com/people/yemilice")
bsObj = BeautifulSoup(html)
for link in bsObj.find("div",{"id":"zh-profile-answers-inner-list"}).findAll("a",
                        href=re.compile("^(/question/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
