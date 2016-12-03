from http.cookiejar import *
from urllib.request import *


filename = 'cookie.txt'

cookie = MozillaCookieJar(filename)

handler = HTTPCookieProcessor(cookie)

opener = build_opener(handler)

response = opener.open("http://www.baidu.com")

cookie.save(ignore_discard=True, ignore_expires=True)