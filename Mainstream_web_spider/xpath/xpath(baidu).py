# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json

def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)



