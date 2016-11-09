from urllib.request import urlopen
response = urlopen("http://www.baidu.com")
print(response.read())