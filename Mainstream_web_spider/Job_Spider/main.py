from multiprocessing import Pool
from lagou_page import Url_list
from Page_persion import job_page,Job_message,Job_Url,Job_info

db_urls = [item['Url'] for item in Job_Url.find()]
x = set(db_urls)
rest_of_urls = x

def get_links_from(channel):
    for num in range(1,30):
        job_page(channel,num)

if __name__ == '__main__':
    pool = Pool()
    pool.map(Job_message,x)
    # pool.map(get_links_from,Url_list.split())
    pool.close()
    pool.join()
    connect=False
