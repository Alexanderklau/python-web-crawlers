# coding=utf-8
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from ..items import DoubanmovieItem
import re


class doubanSpider(BaseSpider):
    name = "douban1"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://www.douban.com/group/ProductManager/",
    ]

    # 在页面中找小组
    def __get_id_from_group_url(self, url):
        m = re.search("^http://www.douban.com/group/([^/]+)/$", url)
        if (m):

            # m.group(1) 的值是ProductManager
            return m.group(1)
        else:
            return 0

    def parse(self, response):

        self.log("Fetch group home page: %s" % response.url)

        hxs = HtmlXPathSelector(response)
        item = DoubanmovieItem()

        # get group name
        # 为了得到小组名称，使用hxs.select('//h1/text()')得到h1标题的内容，然后用re("^\s+(.*)\s+$")过滤到标题的空格
        item['groupName'] = hxs.select('//h1/text()').re("^\s+(.*)\s+$")[0]

        # get group id
        # 需要测试这个reponse.url在使用的时候是否是返回的下一个 待爬取的url
        item['groupURL'] = response.url
        # response.url中的内容 ： http://www.douban.com/group/WHV/
        groupid = self.__get_id_from_group_url(response.url)

        # get group members number
        members_url = "http://www.douban.com/group/%s/members" % groupid
        # a[contains(@href, "%s")]是模糊查询
        members_text = hxs.select('//a[contains(@href, "%s")]/text()' % members_url).re("\((\d+)\)")
        # member_text[0]值成员数
        item['totalNumber'] = members_text[0]

        # get relative groups
        # 为了得到小组的相关小组，使用hxs.select('//div[contains(@class, "group-list-item")]')得到一个小组列表，
        # 然后在for循环中select小组的URL，并append到item['RelativeGroups']数组中
        item['RelativeGroups'] = []
        groups = hxs.select('//div[contains(@class, "group-list-item")]')
        for group in groups:
            url = group.select('div[contains(@class, "title")]/a/@href').extract()[0]
            item['RelativeGroups'].append(url)
        # item['RelativeGroups'] = ','.join(relative_groups)
        return item