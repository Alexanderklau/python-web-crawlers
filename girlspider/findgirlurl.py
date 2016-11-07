from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

html = urlopen("http://www.mmkao.net/")
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read())
        Name = bsobj.head.title
    except AttributeError as e:
        return None
    return Name
Name = getTitle("http://www.mmkao.net/")
if Name == None:
    print("Title could not be found")
else:
    print(Name)