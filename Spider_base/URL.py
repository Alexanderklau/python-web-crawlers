from urllib.request import urlopen,urlretrieve,Request
from requests import Session
import requests
from bs4 import BeautifulSoup
import re

html = requests.get('http://tieba.baidu.com')
print(html.text)