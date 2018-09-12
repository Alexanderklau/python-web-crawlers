from requests import Session
from bs4 import BeautifulSoup

session = Session()
headres = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}

url = "http://www.sina.com.cn/"
req = session.get(url,headres=headres)

bsObj = BeautifulSoup(req.text)
print(bsObj.find("table",{"class":"finance-form"}).get_text)
