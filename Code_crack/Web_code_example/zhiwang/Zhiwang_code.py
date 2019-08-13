# coding: utf-8

__author__ = "lau.wenbo"


from PIL import Image
import tesserocr

# 图形验证码的破解逻辑
# 无干扰线

image = Image.open('CheckCode.jpg')
image = image.convert('L')
image.show()
threshold = 80
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)
