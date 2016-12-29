from multiprocessing import Pool
from channel_extract import Url_list
from page_parsing import get_links_from,get_item_info,item_info,url_list


db_urls = [item['url'] for item in url_list.find()]
# index_urls = [item['url'] for item in item_info()]
x = set(db_urls)
# y = set(index_urls)
rest_of_urls = x

def get_all_links_from(channel):
    for num in range(1,101):
        get_links_from(channel,num)

if __name__ == '__main__':
    pool = Pool()
    # pool = Pool(processes=6)
    pool.map(get_all_links_from,Url_list.split())
    # pool.map(get_item_info, x)
    pool.close()
    pool.join()
    connect = False
    # pool.close()
    # pool.join()




