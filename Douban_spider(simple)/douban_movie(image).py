import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseurl = "https://www.zhihu.com/question/26055420"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://"+source
    else:
        url = baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path = absoluteUrl.replace("www.","")
    path = path.replace(baseUrl,"")
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen("https://www.zhihu.com/question/26055420")
bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseurl, download["src"])
    if fileUrl is not None:
        print(fileUrl)

urlretrieve(fileUrl,getDownloadPath(baseurl,fileUrl,downloadDirectory))
