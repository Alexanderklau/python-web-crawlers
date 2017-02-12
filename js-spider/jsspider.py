# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
import json
from bs4 import BeautifulSoup
headers = {
    'Referer':'https://detail.tmall.com/item.htm?id=536318168355&areaId=510100&user_id=1114511827&cat_id=2&is_b=1&rn \
=03c1e7a4b3f5b5239340ca03dabd0be8&sku_properties=1627207:28328;5919063:3266781;12304035:48072'
}
url = requests.get('https://mdskip.taobao.com/core/initItemDetail.htm?isRegionLevel=false&tryBeforeBuy=false&addressLevel=4&service3C=true&isSecKill=false&tmallBuySupport=true&showShopProm=false&itemId=536318168355&cachedTimestamp=1486865253366&queryMemberRight=true&household=false&sellerPreview=false&isForbidBuyItem=false&isApparel=false&isUseInventoryCenter=false&cartEnable=true&isAreaSell=false&offlineShop=false&isPurchaseMallPage=false&callback=setMdskip',headers=headers).content
x = url[12:-20]
print(x)


# if __name__ == '__main__':