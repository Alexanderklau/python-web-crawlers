import random
proxy_list = [
    'http://222.169.193.162:8099',
    'http://171.38.154.86:8123',
    'http://60.176.164.2:8118',
    'http://180.104.106.130:8998',

]
proxy_ip = random.choice(proxy_list)
proxies = {'http:':proxy_ip}