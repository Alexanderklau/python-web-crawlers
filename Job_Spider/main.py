from multiprocessing import Pool
from lagou_page import Url_list
from Page_persion import job_page
from .Page_persion import Job_message

def get_links_from(channel):
    for num in range(1,30):
        job_page(channel,num)

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_links_from,Url_list.split())
