#-*-coding:utf-8-*-
from urllib.request import urlretrieve,urlopen
from bs4 import BeautifulSoup
import re
import sys
import urllib.request
import http.cookiejar

temp = 0
for x in range(1,300):
    temp += x
    url = "http://www.3dmgame.com/gl/?tid=26&totalpage=527&page=" + str(temp)
    req = urllib.request.Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    html = urlopen(req)
    bsObj = BeautifulSoup(html)
    for link in bsObj.find("div",{"class":"QZlisttxt"}).findAll("a",href=re.compile("(/gl/)(\d)+")):
        if 'href' in link.attrs:
            href = link.attrs['href']
            content = urlopen(href)
            title = href[-12:]
            file = open(r'gl_txt/' + title,"wb").writelines(content)


        #http://www.3dmgame.com /gl/201611/3607132.html


