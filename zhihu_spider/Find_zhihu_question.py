from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.zhihu.com/people/yemilice")
bsObj = BeautifulSoup(html)
#利用正则表达式寻找出id是zh-profile-activity-page-list的，以/question/开头的URL
for link in bsObj.find("div",{"id":"zh-profile-activity-page-list"}).findAll("a",href=re.compile("^(/question/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])


