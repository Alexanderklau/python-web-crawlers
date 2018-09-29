# coding: utf-8

__author__ = 'lau.wenbo'

"""
破解简单的图形验证码,拿到电话号码并且验证
"""

import sys
from pytesseract import *
import requests
import os
import re
from PIL import Image
from PIL import ImageEnhance
import pkg_resources
url = 'http://t.51chuli.com/contact/d91779cced1ade729yz45q72bn3o5o1z.gif'
html = requests.get(url)
with open('vercode.gif', 'wb') as f:
    f.write(html.content)
    f.flush()
    os.fsync(f.fileno())
if os.path.isfile('vercode.gif'):
    image = Image.open('vercode.gif')
    image = image.convert('L')
    threshold = 250
    initTable = lambda x:0 if x < threshold else 1
    binaryImage = image.point(initTable, '1')
    vcode = image_to_string(binaryImage, lang="eng", config='-psm 7')
    print (vcode.replace(' ',''))
