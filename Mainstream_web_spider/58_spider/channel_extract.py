import requests
from bs4 import BeautifulSoup
start_urls = 'http://cd.58.com/sale.shtml'

def Find_urls(url):
    wb_data = requests.get(start_urls)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    print(type(links))
    for link in links:
        page_url = 'http://cd.58.com' + link.get('href')
        # print(page_url)

Url_list = """
    http://cd.58.com/shouji/
    http://cd.58.com/danche/
    http://cd.58.com/fzixingche/
    http://cd.58.com/diandongche/
    http://cd.58.com/sanlunche/
    http://cd.58.com/peijianzhuangbei/
    http://cd.58.com/diannao/
    http://cd.58.com/bijiben/
    http://cd.58.com/pbdn/
    http://cd.58.com/diannaopeijian/
    http://cd.58.com/zhoubianshebei/
    http://cd.58.com/shuma/
    http://cd.58.com/shumaxiangji/
    http://cd.58.com/mpsanmpsi/
    http://cd.58.com/youxiji/
    http://cd.58.com/jiadian/
    http://cd.58.com/dianshiji/
    http://cd.58.com/ershoukongtiao/
    http://cd.58.com/xiyiji/
    http://cd.58.com/bingxiang/
    http://cd.58.com/binggui/
    http://cd.58.com/chuang/
    http://cd.58.com/ershoujiaju/
    http://cd.58.com/bangongshebei/
    http://cd.58.com/diannaohaocai/
    http://cd.58.com/bangongjiaju/
    http://cd.58.com/ershoushebei/
    http://cd.58.com/yingyou/
    http://cd.58.com/yingeryongpin/
    http://cd.58.com/muyingweiyang/
    http://cd.58.com/muyingtongchuang/
    http://cd.58.com/yunfuyongpin/
    http://cd.58.com/fushi/
    http://cd.58.com/nanzhuang/
    http://cd.58.com/fsxiemao/
    http://cd.58.com/xiangbao/
    http://cd.58.com/meirong/
    http://cd.58.com/yishu/
    http://cd.58.com/shufahuihua/
    http://cd.58.com/zhubaoshipin/
    http://cd.58.com/yuqi/
    http://cd.58.com/tushu/
    http://cd.58.com/tushubook/
    http://cd.58.com/wenti/
    http://cd.58.com/yundongfushi/
    http://cd.58.com/jianshenqixie/
    http://cd.58.com/huju/
    http://cd.58.com/qiulei/
    http://cd.58.com/yueqi/
    http://cd.58.com/chengren/
    http://cd.58.com/nvyongpin/
    http://cd.58.com/qinglvqingqu/
    http://cd.58.com/qingquneiyi/
    http://cd.58.com/chengren/
    http://cd.58.com/xiaoyuan/
    http://cd.58.com/ershouqiugou/
    http://cd.58.com/tiaozao/
"""
Find_urls(start_urls)

