#coding:utf-8
from urllib.request import urlopen,Request,HTTPCookieProcessor,install_opener,build_opener
from urllib.parse import urlencode
import http.cookiejar
import re
import time
import json

class Email163:
    header = {'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    }
    used = ''
    cookie = None
    sid = None
    mailBaseUrl = 'http://twebmail.mail.163.com'

    def __init__(self):
        self.cookie = http.cookiejar.CookieJar()
        cookiePro = HTTPCookieProcessor(self.cookie)
        install_opener(build_opener(cookiePro))

    def login(self,user,pwd):
        postdata = urlencode({
            'username':user,
            'password':pwd,
            'type':1})
        req = Request(
            url= 'https://ssl.mail.163.com/entry/coremail/fcg/ntesdoor2?\
            funcid=loginone&language=-1&passtype=1&iframe=1&product=mail163&from=web&df=\
            email163&race=-2_45_-2_hz&module=&uid='+user+'&style=10&net=t&skinid=null',
            data = postdata,
            headers=self.header,
        )
        res = str(urlopen(req).read())
        # print res
        patt = re.compile('sid=([^"]+)', re.I)
        patt = patt.search(res)

        uname = user.split('@')[0]
        self.user = user
        if patt:
            self.sid = patt.group(1).strip()
            # print self.sid
            print('%s Login Successful.....' % (uname))
        else:
            print('%s Login failed....' % (uname))

def getInBox(self):
        print('\nGet mail lists.....\n')
        sid = self.sid
        url = self.mailBaseUrl + '/jy3/list/list.do?sid=' + sid + '&fid=1&fr=folder'
        res = urlopen(url).read()
        # 获取邮件列表
        mailList = []
        patt = re.compile('<div\s+class="tdLike Ibx_Td_From"[^>]+>.*?href="([^"]+)"[^>]+>(.*?)<\/a>.*?<div\s+class="tdLike Ibx_Td_Subject"[^>]+>.*?href="[^>]+>(.*?)<\/a>',
            re.I | re.S)
        patt = patt.findall(res)
        if patt == None:
            return mailList
        for i in patt:
            line = {
                'from': i[1].decode('utf8'),
                'url': self.mailBaseUrl + i[0],
                'subject': i[2].decode('utf8')
            }
            mailList.append(line)
            return mailList

    def getMailMsg(self, url):
        '''
            下载邮件内容
        '''
        content = ''
        print('\n Download.....%s\n' % (url))
        res = urlopen(url).read()

        patt = re.compile('contentURL:"([^"]+)"', re.I)
        patt = patt.search(res)
        if patt == None:
            return content
        url = '%s%s' % (self.mailBaseUrl, patt.group(1))
        time.sleep(1)
        res = urlopen(url).read()
        Djson = json.JSONDecoder()
        jsonRes = Djson.decode(res)
        if 'resultVar' in jsonRes:
            content = Djson.decode(res)['resultVar']
            time.sleep(3)
            return content
    # 初始化
mail163 = Email163()
    # 登录
mail163.login('xxxxx@163.com', 'xxxx')
time.sleep(2)

    # 获取收件箱
elist = mail163.getInBox()

    # 获取邮件内容
for i in elist:
    print('主题：%s   来自：%s  内容：\n %s' % (
        i['subject'].encode('utf8'), i['from'].encode('utf8'), mail163.getMailMsg(i['url']).encode('utf8')))

