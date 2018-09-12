import requests
from bs4 import BeautifulSoup
import time

# data =  (''+' '.join(map(lambda x: '0'+str(x) if len(str(x))==1 else str(x),range(1,41)))+'')
# print(data)
for i in range(1,30):
    if i < 10:
        print('0' + str(i))
    else:
        print(i)

# print(data)
