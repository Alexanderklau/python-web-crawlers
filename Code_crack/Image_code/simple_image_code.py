# coding: utf-8

__author__ = 'lau.wenbo'

"""
破解简单的图形验证码
"""

import tesserocr
from PIL import Image


# image = Image.open('../Example_image/Image/simple3615.jpg')
image = Image.open('1.jpg')
result = tesserocr.image_to_text(image)
print(result)

