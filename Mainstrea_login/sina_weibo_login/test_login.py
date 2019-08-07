# coding: utf-8
__author__ = 'Yemilice_lau'

import requests


z = requests.get(
    "https://meican.com/preorder/api/v2.1/orders/show?uniqueId=ebface36a55d&type=CORP_ORDER&progressMarkdownSupport=true&x=1565143351392")

print(z.text)