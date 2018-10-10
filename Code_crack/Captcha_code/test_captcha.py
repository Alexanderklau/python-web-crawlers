# coding: utf-8

__author__ = 'lau.wenbo'


import pytesseract
from PIL import Image


image = Image.open("2.jpg")
# 灰度处理，更加方便识别
images = image.convert('L')
table = []
threshould = 80
for i in range(256):
    if i < threshould:
        table.append(0)
    else:
        table.append(1)

images = images.point(table, "1")
result = pytesseract.image_to_string(images)
print(result)