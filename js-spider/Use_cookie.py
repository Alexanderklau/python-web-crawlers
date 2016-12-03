#-*-coding:utf-8-*-
from http.cookiejar import *
from urllib.request import *



cookie = MozillaCookieJar()

cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = Request("http://www.baidu.com")

opener = build_opener(HTTPCookieProcessor(cookie))
response = opener.open(req)
print (response.read())