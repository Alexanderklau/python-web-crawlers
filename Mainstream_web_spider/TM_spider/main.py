# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from multiprocessing import Pool
from TM import Goods_message,get_goodsUrl,TM_url,TM_info
db_urls = [item['Url'] for item in TM_url.find()]
x = set(db_urls)
rest_of_urls = x
if __name__ == '__main__':
    pool = Pool()
    pool.map(Goods_message,x)
    # pool.map(get_links_from,Url_list.split())
    pool.close()
    pool.join()
    connect=False








# if __name__ == '__main__':