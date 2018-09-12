# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
import re
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
header = {'User-Agent':user_agent}
bsobj = requests.get('https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=rank&page_limit=20&page_start=20',headers = header)
html = bsobj.text
name = re.findall('"title":"(.*?)"',html,re.S)
star = re.findall('"rate":"(.*?)"',html,re.S)
print(name,star)









# if __name__ == '__main__':