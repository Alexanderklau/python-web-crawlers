# coding: utf-8

__author__ = 'lau.wenbo'

#!/usr/bin/env python2
# -*- coding=utf-8 -*-

from queue import Queue
import time
from lxml import etree
import requests
import gevent

#　打上猴子补丁
from gevent import monkey
monkey.patch_all()

class DouBanSpider(object):
    def __init__(self):
        # 创建一个队列用来保存进程获取到的数据
        self.q = Queue()
        self.headers = {
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/top250?start=225&filter=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
        }

    def run(self,url):
        self.parse_page(url)

    def send_request(self,url):
        '''
        用来发送请求的方法
        :return: 返回网页源码
        '''
        # 请求出错时，重复请求３次,
        i = 0
        while i <= 3:
            try:
                print("[INFO]请求url:"+url)
                html = requests.get(url=url,headers=self.headers).content
            except Exception as e:
                print('[INFO] %s%s'% (e,url))
                i += 1
            else:
                return html

    def parse_page(self,url):
        '''
        解析网站源码，并采用ｘｐａｔｈ提取　电影名称和平分放到队列中
        :return:
        '''
        response = self.send_request(url)
        html = etree.HTML(response)
        #　获取到一页的电影数据
        node_list = html.xpath("//div[@class='info']")
        for move in node_list:
            # 电影名称
            title = move.xpath('.//a/span/text()')[0]
            # 评分
            score = move.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]

            # 将每一部电影的名称跟评分加入到队列
            self.q.put(score + "\t" + title)


    def main(self):


        base_url = 'https://movie.douban.com/top250?start='
        # 构造所有ｕｒｌ
        url_list = [base_url+str(num) for num in range(0,225+1,25)]
        # 创建协程并执行
        job_list = [gevent.spawn(self.run,url) for url in url_list]
        # 让线程等待所有任务完成，再继续执行。
        gevent.joinall(job_list)

        while not self.q.empty():
            print(self.q.get())

if __name__=="__main__":
    start = time.time()
    douban = DouBanSpider()
    douban.main()
    print('[info]耗时：%s'%(time.time()-start))
