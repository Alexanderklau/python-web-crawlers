from urllib.request import urlopen,urlretrieve,Request
from bs4 import BeautifulSoup
import re
for page in range(2, 30):
    Url = "http://pic.ali213.net/list/game/index_%s.html" % (page)
    print(Url)
    req = Request(Url,headers = {'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',})
    html = urlopen(req)
    bsObj = BeautifulSoup(html)
    for image in bsObj.findAll("img",src=re.compile("(.+?\.jpg)")):
        if 'src' in image.attrs:
            imglist = []
            imglist = image.attrs['src']
            name = imglist[-20:]
            file = urlretrieve(imglist,r'image/' + name)






