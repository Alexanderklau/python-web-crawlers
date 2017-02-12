import requests
from bs4 import BeautifulSoup
import re
import time
import pymongo
from lagou_page import headers,proxies

client = pymongo.MongoClient('localhost', 27017)
Job = client['Jobs']
Job_Url = Job['Job_Url']
Job_info = Job['Job_info']


def job_page(channel,pages):
    # https://www.lagou.com/zhaopin/Java/2/
    # https://www.lagou.com/zhaopin/Java/
    list_view = '{}{}'.format(channel, str(pages))
    time.sleep(2)
    wb_data = requests.get(list_view, headers=headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('a','position_link'):
        for link in soup.select('a.position_link'):
            href = link.get('href').split('?')[0]
            href = re.sub('//','http://',href)
            Job_Url.insert_one({'Url':href})
            print(href)
    else:
        pass
    # Job_name = soup.select('a.position_link h2')[0].text
    # for i in list(soup.select('span.add')):Job_area=i.text
    # for i in list(soup.select('span.money')):Job_price = i.text
    # for i in list(soup.select('div.company_name > a')):Job_unit = i.text
    # print(Job_name)

def Job_message(url):
    wb_data = requests.get(url,headers=headers,proxies = proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(2)
    Job_name = soup.select('span.name')[0].text if soup.find_all('span','name') else None
    Job_company = soup.select('div.company')[0].text if soup.find_all('div','company') else None
    Job_price = soup.select('span.salary')[0].text if soup.find_all('span','salary') else None
    Job_date = soup.select('p.publish_time')[0].text if soup.find_all('p','publish_time') else None
    Job_area = list(soup.select('div.work_addr')[0].stripped_strings) if soup.find_all('div','work_addr') else None
    Job_info.insert_one({'Job_name':Job_name,
                         'Job_company':Job_company,
                         'Job_price':Job_price,
                         'Job_date':Job_date,
                         'Job_area':Job_area,
                         'url':url})
    print({'Job_name':Job_name,
                         'Job_company':Job_company,
                         'Job_price':Job_price,
                         'Job_date':Job_date,
                         'Job_area':Job_area,
                         'url':url})
# Job_message('http://www.lagou.com/jobs/1475498.html')



