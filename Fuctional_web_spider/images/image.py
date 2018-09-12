from urllib.request import urlopen,urlretrieve,Request
from bs4 import BeautifulSoup
import random

def Download_Html(url):
    ip = ['121.31.159.197', '175.30.238.78', '124.202.247.110']
    header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'X-Forwared-For' : ip[random.randint(0,2)]}
    request = Request(url,None,header)
    response = urlopen(request)
    return response.read()
def Download_file():
    pass