import requests
from bs4 import BeautifulSoup
import re
wb_data = requests.get('http://www.mmkao.net/RQ-STAR/201609/11924.html')
soup = BeautifulSoup(wb_data.text,'lxml')
title = soup.select('title')[0].text
ID = '\d'
str1 = ""
tx = re.findall(ID,title)
str1 = str1.join(tx)
if str1[0] == '0':
    str2 = str1.strip('0')
    print(str2)
else:
    print(str1)


# print(str1)