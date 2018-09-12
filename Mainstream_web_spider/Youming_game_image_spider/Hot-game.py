from bs4 import BeautifulSoup
from urllib.request import urlopen,urlretrieve,Request
import re

url = "http://www.3dmgame.com/games/hot/"
req = Request(url,headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
html = urlopen(req)
bsObj = BeautifulSoup(html)
for name in bsObj.find("div",{"id":"list"}).findAll("h3"):
    Gamename = name.get_text()
    for content in bsObj.find("div",{"id":'list'}).findAll("dl"):
        Gamecontent = content.get_text()

    file = open("Hot-game.txt","a+").writelines(Gamename and Gamecontent)




