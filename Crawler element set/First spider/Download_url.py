from urllib.request import *
url = 'https://www.baidu.com/'
html = urlopen(url).read()
print(html)
