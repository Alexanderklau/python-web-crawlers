# coding: utf-8

__author__ = 'lau.wenbo'

"""
这里用简单的豆瓣爬虫做例子，爬取豆瓣电影top250
"""

import aiohttp
import requests
import time
from queue import Queue
from threading import Thread
from lxml import etree


class Doubanmovie(Thread):
    def __init__(self, url, q):
        super(Doubanmovie, self).__init__()
        self.url = url
        self.q = q
        self.headers = {
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Host":"movie.douban.com"
        }

    def run(self):
        self.parse_page()

    def send_request(self, url):
        # 出错时请求三次
        i = 0
        while i <= 3:
            try:
                # print("请求的Url是{url}".format(url = url))
                html = requests.get(url=url, headers=self.headers).content
            except Exception as e:
                print("Error!message{message}}".format(message=e))
                i += 1
            else:
                return html

    def parse_page(self):
        response = self.send_request(self.url)
        html = etree.HTML(response)
        # 　获取到一页的电影数据
        node_list = html.xpath("//div[@class='info']")
        for move in node_list:
            # 电影名称
            title = move.xpath('.//a/span/text()')[0]
            # 评分
            score = move.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]

            # 将每一部电影的名称跟评分加入到队列
            self.q.put(score + "\t" + title)


def main():
    # 创建一个队列用来保存进程获取到的数据
    q = Queue()
    base_url = 'https://movie.douban.com/top250?start='
    # 构造所有ｕｒｌ
    url_list = [base_url + str(num) for num in range(0, 225 + 1, 25)]


    # 保存线程
    Thread_list = []
    # 创建并启动线程
    for url in url_list:
        p = Doubanmovie(url, q)
        p.start()
        Thread_list.append(p)

    # 让主线程等待子线程执行完成
    for i in Thread_list:
        i.join()

    while not q.empty():
        print(q.get())


if __name__ == "__main__":
    start = time.time()
    main()
    print('[info]耗时：%s' % (time.time() - start))