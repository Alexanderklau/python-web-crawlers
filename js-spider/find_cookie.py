from http.cookiejar import *
from urllib.request import *

cookie = CookieJar()
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)
