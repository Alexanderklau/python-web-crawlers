# -*- coding: utf-8 -*-

from urllib.request import *
import urllib
import re
import _thread
import time
import json


class Spider_Model:#定义一个爬虫模块
    def __init__(self):#初始化
        self.page = 1
        self.pages = []
        self.enable = False



    def GetPage(self, page):
        myUrl = "http://www.jiu-tuo.com/list-jiutuo--" + page
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        req = Request(myUrl, headers=headers)#指定固定的域名，发送请求
        myResponse = urlopen(req)#响应请求
        myPage = myResponse.read()#读取请求
        # print myPage  
        unicodePage = myPage.decode("utf-8")
        # 找出所有class="cstdrt show63"的div标记
        # re.S是任意匹配模式，也就是.可以匹配换行符
        myItems = re.findall('<td.*?class="stdrt show.*?".*?>(.*?)</td>', unicodePage, re.S)
        items = []

        return myItems

        # 用于加载新的事迹

    def LoadPage(self):
        # 如果用户未输入quit则一直运行      
        while self.enable:
            # 如果pages数组中的内容小于2个  
            # print len(self.pages)  
            if len(self.pages) < 2:
                try:
                    # 获取新的页面中的事迹
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print('无法链接！')
            else:
                time.sleep(5)

                # def ShowPage(self,nowPage,page):

    # print u'第%d页' % page,json.dumps(nowPage, encoding="UTF-8", ensure_ascii=False)

    def ShowPage(self, nowPage, page):
        i = 0
        # print len(nowPage)  
        for i in range(0, len(nowPage)):
            if i < len(nowPage):
                print (u'第%d页,第%d个案例' % (page, i), nowPage[i].replace("\n\n", ""))
                i += 1
            else:
                break

    def Start(self):
        self.enable = True
        page = self.page
        print (u'正在加载中请稍候......')
        # 新建一个线程在后台加载段子并存储      
        _thread.start_new_thread(self.LoadPage, ())
        # ----------- 加载处理 -----------
        while self.enable:
            # 如果self的page数组中存有元素      
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage, page)
                page += 1


                # ----------- 程序的入口处 -----------


print( u"""
---------------------------------------   
   程序：爬虫
   版本：0.3   
   作者：
   日期：
   语言：Python 2.7   
   操作：输入quit退出
   功能：按下回车依次浏览热点
---------------------------------------   
""")

print (u'请按下回车浏览今日内容：')
input(' ')
myModel = Spider_Model()
myModel.Start()      