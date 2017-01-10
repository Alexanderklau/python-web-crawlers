# -*- coding:utf-8 -*-
import urllib
import urllib2
import time
import json
import thread
import re
class Spider_Model:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False
    def GetPage(self,page):
        baseUrl = "http://www.chinness.cn/web/query.asp?page=" + page
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
        headers = {'User-Agent':user_agent}
        req = urllib2.Request(baseUrl,headers=headers)
        BodyResponse = urllib2.urlopen(req)
        BodyPage = BodyResponse.read()
        unicodePage = BodyPage.decode('utf-8')
        BodyItems = re.findall('<table.*?align="center".*?>(.*?)</table>',unicodePage,re.S)
        Itmes = []
        return BodyItems
    def loadPage(self):
        while self.enable:
            if len(self.pages) < 2:
                try:
                    BodyPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(BodyPage)
                except:
                    print "can't internet"
            else:
                time.sleep(5)
    def showPage(self,nowPage,page):
        i = 0
        for i in range(0,len(nowPage)):
            if i < len(nowPage):
                print u'this is %d page,is %d body' % (page,i),nowPage[i].replace("\n\n","")
                i += 1
            else:
                break
    def Start(self):
        self.enable = True
        page = self.page
        thread.start_new_thread(self.loadPage(),())
        while self.enable:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.showPage(nowPage,page)
                page += 1

print u"""
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

print u'请按下回车浏览今日内容：'
raw_input(' ')
myModel = Spider_Model()
myModel.Start()




