import time
from page_parsing import url_list,item_info

while True:
    print('message:',item_info.find().count())
    print('URL:',url_list.find().count())
    time.sleep(5)