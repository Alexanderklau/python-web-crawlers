import http.cookiejar

from urllib.request import urlopen,build_opener,HTTPCookieProcessor
from urllib.parse import urlencode
filename = 'cookit.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = build_opener(HTTPCookieProcessor(cookie))
postdata = urlencode({
    'stuid':'',
    'pwd':'',
})
loginUrl = 'url'
result = opener.open(loginUrl,postdata)

