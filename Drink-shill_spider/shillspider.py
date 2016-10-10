from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re
import datetime
import csv
import time
from urllib.request import Request
class Spider_model:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.endable = False
    def ShillPage(self,page):
        BaseUrl = "http://www.jiu-tuo.com/list-jiutuo--" + page
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
        headers = {'User-Agent':user_agent}
        req = Request(BaseUrl,headers=headers)
        myResponse = urlopen(req)
        myPage = myResponse.read()
        unicodePage = myPage.decode('utf-8')

        MyItems = re.findall("td",{"class":"stdrt"},unicodePage,re.S)
        items = []
        return MyItems
    def lodePage(self):
        while self.enable:
            if (len(self.pages) < 2):
                try:
                    mypage = self.ShillPage(str(self.page))
                    self.page += 1
                    self.pages.append(mypage)
                except:
                    print("cant internet")
                else:
                    time.sleep(5)
a = Spider_model()
a.Start()




# html = urlopen("http://www.jiu-tuo.com/list-jiutuo--1")
# bsObj = BeautifulSoup(html)
# table = bsObj.findAll("td",{"class":"stdrt"})
# csvFile = open("shill.csv",'wt',newline="",encoding='utf-8')
# write = csv.writer(csvFile)

# 查找固定的信息
# message = bsObj.findAll("td",{"class":"stdrt"})
# for mess in message:
#  print(mess.get_text())

# 查找固定电话
# Phonenumber = bsObj.findAll("td",{"style":"color:red;"})
# for number in Phonenumber:
#     print(number.get_text())

