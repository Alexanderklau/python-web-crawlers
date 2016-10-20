from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.sina.com.cn")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        URL = link.attrs['href']
        print(URL)
        fout = open("Find_Url","w")
        fout.write("%s" %URL)
        fout.close()


