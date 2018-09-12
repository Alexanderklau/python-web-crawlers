from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Cookie':'_gscu_1672982541=683861774rzdp813; ASPSESSIONIDCCCARRBR=LFFEFOHDPJJMNIPJNJCOKFHF',
}
url_saves = '**************************'
wb_data = requests.get(url_saves,headers=headers)
wb_data.encoding = 'gb2312'
soup = BeautifulSoup(wb_data.text,'lxml')
title = soup.select('td')
print(title)