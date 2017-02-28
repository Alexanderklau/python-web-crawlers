# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.5'
}
def get_page(name,page):
    try:
        lise_view = '{}/{}.html'.format(name,str(page))
        wb_data = requests.get(lise_view,headers = headers)
        html = BeautifulSoup(wb_data.text,'lxml')
        # print(html)
        urls = html.select('ul.photo li a')
        for url in urls:
            ID = url.get('href')
            if ID == None:
                return ID
            else:
                return ID
    except requests.HTTPError as e:
        if hasattr(e,'reson'):
            print(u'连接失败,错误代码',e.reson)
            return None
def image_list(name,ID):
    lise_view = '{}/{}'.format(name,ID)
    wb_data = requests.get(lise_view,headers = headers)
    html = BeautifulSoup(wb_data.text,'lxml')
    pages = html.select('ul.image strong')
    ImageIds = html.select('title')[0].text
    ImageId = re.findall('\d',ImageIds)
    Id = ''.join(ImageId)
    page = re.search('<strong>(.*?)</strong>',str(pages)).group(1)
    pages = (' '.join(map(lambda x: '0' + str(x) if len(str(x)) == 1 else str(x), range(1, (int(page) * 6) + 1))))
    pages = pages.split(' ')
    for i in pages:
        pagename = i + '.jpg'
        Download_url = 'http://img.mmkao.net/photo/beautyleg/beautyleg' + Id +'/' + pagename
        return Download_url
    #"http://img.mmkao.net/photo/beautyleg/beautyleg1355/01.jpg "
def Download(url):
    pass


if __name__ == '__main__':
    for i in range(2, 47):
        ID = get_page('http://mmkao.net/Beautyleg/', i)
        list = image_list('http://mmkao.net/Beautyleg/',ID)
        print(list)
# http://mmkao.net/Beautyleg/201612/12425.html
# image_list('http://mmkao.net/Beautyleg/','201612/12425')
# get_page('http://mmkao.net/Beautyleg',2)









