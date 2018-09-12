import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.request import urlopen,urlretrieve
def find_url():
    for i in range(2,47):
        start_url = "http://www.mmkao.net/Beautyleg/" + str(i) + ".html"
        wb_data = requests.get(start_url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        links = soup.select('ul.photo > li a')
        for link in links:
            pageUrl = "http://www.mmkao.net/Beautyleg/" + link.get('href')
            wd_text = requests.get(pageUrl)
            wd_text.encoding = 'gb2312'
            selectx = BeautifulSoup(wd_text.text,'lxml')
            title = selectx.select('title')[0].text
            # print(title)
            ID = '\d'
            tx = re.findall(ID, title)
            str1 = ""
            str1 = str1.join(tx)
            for i in range(1, 10):
                imageUrl = "http://img.mmkao.net/photo/beautyleg/beautyleg" + str(str1) + "/0" + str(i) + ".jpg"
                connect = urlopen(imageUrl)
                f = open(r'Girl/' + str1 + str(i) + '.jpg',"wb")
                f.write(connect.read())
                f.close()






find_url()