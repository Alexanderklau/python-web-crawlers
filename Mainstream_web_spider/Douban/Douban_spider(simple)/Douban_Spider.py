from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import threading
import time
import urllib.request

class Douban_spider:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False
    def GetPage(self,page):
        baseUrl = "https://movie.douban.com/tag/喜剧?start=" + page
        user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
        headers = {'User-Agent':user_agent}
        req = urllib.request(baseUrl,headers=headers)
        MovieResponse = urlopen(req)
        MoviePage = MovieResponse.read()
        unicodePage = MoviePage.decode('UTF-8')
        MovieItems = re.findall('<div.*?class="pl2">(.*?)</div>',unicodePage,re.S)
        return MovieItems
    def loadPage(self):
        while self.enable:
            if len(self.pages) < 2:
                try:
                    moviePage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(moviePage)
                except:
                    print("Can't internet")
                else:
                    time.sleep(5)
    def showPage(self,nowPage,page):
        i = 0
        for i in range(0,len(nowPage)):
            if i < len(nowPage):
                print('This is %d page,is %d movie'% (page,i),nowPage[i].replace("\n\n",""))
                i += 1
            else:
                break
    def Start(self):
        self.enable = True
        page = self.page
        threading._start_new_thread(self.loadPage(),())
        while self.enable:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.showPage(nowPage,page)
                page += 1
print(u"""
    ---------------------------------------
       程序：爬虫
       版本：0.3
       作者：
       日期：
       语言：Python 2.7
       操作：输入quit退出
       功能：按下回车依次浏览热点
    ---------------------------------------
    """
)

print (u'请按下回车浏览今日内容')

myModel = Douban_spider()
myModel.Start()
