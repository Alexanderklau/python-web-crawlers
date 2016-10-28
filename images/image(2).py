#-*- coding:utf-8 -*-
import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImage(html):
    reg = r'src="(.?\.jpg)"'
    reg = reg.encode('UTF-8')
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x = x + 1

html = getHtml("http://www.mmkao.net/sjw/201603/10682.html")
getImage(html)
