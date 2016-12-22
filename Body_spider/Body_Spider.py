from bs4 import BeautifulSoup
import requests
import time

# urls = ['http://www.wmsz.net/web/query.asp?page={}'.format(str(i)) for i in range(1,41)]
url = 'http://www.wmsz.net/web/query.asp?page=1'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Host':'www.wmsz.net',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
}
# def get_arrtactions(url,data=None):
wb_data = requests.get(url,headers=headers)
wb_data.encoding = 'gb2312'
soup = BeautifulSoup(wb_data.text,'lxml')
name = soup.select('div.cxxx ')
print(name)

# for single_url in urls:
#     get_arrtactions(single_url)