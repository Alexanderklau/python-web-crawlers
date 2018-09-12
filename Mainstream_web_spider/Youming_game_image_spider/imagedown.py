
import re
from urllib.request import urlopen,urlretrieve

def getHtml(url):
    page = urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        urlretrieve(imgurl,'%s.jpg' % x)
        x = x + 1

html = getHtml("http://pic.ali213.net/list/game/")
getImg(html)