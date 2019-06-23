# coding: utf-8

__author__ = "lau.wenbo"


import requests
from bs4 import BeautifulSoup
import pickle


def get_url_list():
    url_list = []
    for i in range(1, 46):
        url = "http://www.zggnw.cn/sell/index-htm-page-{num}.html".format(num=i)
        url_list.append(url)
    return url_list

def get_product(url_list):
    product_list = []
    for i in url_list:
        contents = requests.get(url=i)
        soup = BeautifulSoup(contents.text, 'lxml')
        z = (soup.find_all('div',{"class":'sup-pic'}))
        for i in z:
            href = i.a['href']
            product_list.append(href)
    return product_list

def get_etails(url):
    dic = {}
    contents = requests.get(url)
    soup = BeautifulSoup(contents.text, 'lxml')
    z = soup.find_all('div',{"class":"de-info fr"})
    for i in z:
        name = i.h4.get_text()
        date = i.p.span.get_text().split('：')[1]
        message = i.find_all("tr")
        Variety = message[0].find_all('td')[1].get_text()
        Place = message[1].find_all('td')[1].get_text()
        Price = message[2].find_all('td')[1].get_text().split('￥')[1].split('元')[0]
        Order = message[3].find_all('td')[1].get_text()
        period = message[4].find_all('td')[1].get_text()
        dic["name"] = name
        dic["date"] = date
        dic["Variety"] = Variety
        dic["Place"] = Place
        dic["Price"] = Price
        dic["Order"] = Order
        dic["period"] = period
    return dic



# 生成pickle


if __name__ == "__main__":
    z = []
    url_list = get_url_list()
    for i in get_product(url_list):
        message = get_etails(i)
        z.append(message)
    with open('text.pkl', 'wb') as file:
        pickle.dump(z, file)
