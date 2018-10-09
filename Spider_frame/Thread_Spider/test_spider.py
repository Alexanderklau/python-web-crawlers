# coding: utf-8

__author__ = 'lau.wenbo'

import requests
from lxml import etree

url = "https://movie.douban.com/top250?start="

url_list = [url + str(num) for num in range(0, 225 + 1, 25)]

for i in url_list:
    html = requests.get(url=i).content
    htmls = etree.HTML(html)
        #　获取到一页的电影数据
    node_list = htmls.xpath("//div[@class='info']")
    for move in node_list:
        # 电影名称
        title = move.xpath('.//a/span/text()')[0]
        # 评分
        score = move.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]

        print(title, score)