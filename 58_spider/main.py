from multiprocessing import Pool
from channel_extract import Url_list
from page_parsing import get_links_from,get_item_info,item_info,url_list


# db_urls = [item['url'] for item in url_list.find()]
# index_urls = [item['url'] for item in item_info()]
# x = set(db_urls)
# y = set(index_urls)
# rest_of_urls = x - y

def get_all_links_from(channel):
    for num in range(1,101):
        get_links_from(channel,num)


if __name__ == '__main__':
    pool = Pool()
    pool.map(get_item_info,Url_list.split())
    # pool.close()
    # pool.join()




