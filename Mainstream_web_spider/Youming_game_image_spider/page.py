from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import math

temp = 0
for x in range(1,300):
    temp += x
    url = "http://www.3dmgame.com/gl/?tid=26&totalpage=527&page=" + str(temp)
    req = Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    html = urlopen(req)
    bsObj = BeautifulSoup(html)
    title = bsObj.find("div",{"class":"QZlisttxt"}).findAll("p")
    for name in title:
        txt = name.get_text()
        csvfile = open("page.txt","a+")
        csvfile.writelines(txt+'\n')
        csvfile.close()
