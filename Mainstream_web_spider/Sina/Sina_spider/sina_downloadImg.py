import random
from urllib.request import urlopen,Request,urlretrieve
from bs4 import BeautifulSoup
import os
def getAbsoluteURL(baseUrl,source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url
