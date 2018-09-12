import requests
from bs4 import BeautifulSoup
import time
import string
import re

wb_data = requests.get("http://www.mmkao.net/Beautyleg/201611/12263.html")
wb_data.encoding = 'gb2312'
soup = BeautifulSoup(wb_data.text,'lxml')
title = soup.select('title')[0].text
ID = '\d'
tx = re.findall(ID,title)
str1 = ""
str1 = str1.join(tx)
for i in range(1,10):
    imageUrl = "http://img.mmkao.net/photo/beautyleg/beautyleg" + str(str1) + "/0" + str(i) + ".jpg"
    print(imageUrl)
