from multiprocessing import Pool
from channel_list import Url_list
# from Page_parsing import GirlID,get_item_info,get_links_from,GirlUrl
from Page_list import get_links_from,GirlID,GirlUrl

# db_url = [item['url'] for item in GirlUrl.find()]
# x = set(db_url)

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