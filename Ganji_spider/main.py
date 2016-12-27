from multiprocessing import Pool
from Page_parsing import get_links,article_message,Url_list,article_info
from channel_extract import Find_url,url_list

# db_urls = [item['url'] for item in Url_list.find()]
# index_urls = [item['url'] for item in article_info.find()]
# x = set(db_urls)
# y = set(index_urls)
# rest_of_urls = x - y

def get_all_links_from(channel):
    for i in range(1,100):
        get_links(channel,i)

if __name__ == '__main__':
    pool = Pool(processes=6)
    pool.map(get_all_links_from,url_list.split())
    # pool.close()
    # pool.join()