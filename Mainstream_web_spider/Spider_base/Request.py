from urllib.request import urlopen
from urllib.request import Request

request = Request("http://www.baidu.com")
response = urlopen(request)
print(response.read())