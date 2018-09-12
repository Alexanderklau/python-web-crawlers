import json
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'http://i.gamersky.com/apirating/init?callback=jQuery&generalId=853606'
wb_data = urlopen(url).read().decode()
s = wb_data[7:-2]
js = json.loads(str(s))
print(js['Average'])
# print(js)



