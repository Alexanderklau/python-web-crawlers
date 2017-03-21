# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import random
ip_list = [
    'http://222.169.193.162:8099',
    'http://171.38.154.86:8123',
    'http://60.176.164.2:8118',
    'http://180.104.106.130:8998',
]
route_ip = random.choice(ip_list)
proxy_ip = {'http:':route_ip}








# if __name__ == '__main__':