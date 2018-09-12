import urllib.request

req = urllib.request.urlopen('http://www.imooc.com/course/list')
buf = req.read()
buf
import re
buf = buf.decode('UTF-8')
listurl = re.findall(r'src=.+\.jpg', buf)
listurl = re.findall(r'http:.+\.jpg', buf)
i = 0
for url in listurl:
    f = open(r"/home/lau/PycharmProjects/python-web-crawlers/Image_download" + '/' + str(i) + '.jpg', 'wb')
    req = urllib.request.urlopen(url)
    buf = req.read()
    f.write(buf)
    i += 1