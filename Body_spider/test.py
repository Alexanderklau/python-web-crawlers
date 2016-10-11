# encoding:UTF-8
import requests

url = "http://www.baidu.com"
data = requests.urlopen(url).read()
data = data.decode('UTF-8')
print(data)