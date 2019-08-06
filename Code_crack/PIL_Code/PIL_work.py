# coding: utf-8

__author__ = "lau.wenbo"


from PIL import Image

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# 对图片做预处理，去除背景
def pre_concert(img):
    width, height = img.size
    threshold = 30
    for i in range(0, width):
        for j in range(0, height):
            p = img.getpixel((i, j))  # 抽取每个像素点的像素
            r, g, b = p
            if r > threshold or g > threshold or b > threshold:
                img.putpixel((i, j), WHITE)
            else:
                img.putpixel((i, j), BLACK)
    # img.show()
    img.save("pre_fig.jpg")
    return


# 对去除背景的图片做噪点处理
def remove_noise(self, window=1):
    if window == 1:
        window_x = [1, 0, 0, -1, 0]
        window_y = [0, 1, 0, 0, -1]
    elif window == 2:
        window_x = [-1, 0, 1, -1, 0, 1, 1, -1, 0]
        window_y = [-1, -1, -1, 1, 1, 1, 0, 0, 0]

    width, height = self.size
    for i in range(width):
        for j in range(height):
            box = []

            for k in range(len(window_x)):
                d_x = i + window_x[k]
                d_y = j + window_y[k]
                try:
                    d_point = self.getpixel((d_x, d_y))
                    if d_point == BLACK:
                        box.append(1)
                    else:
                        box.append(0)
                except IndexError:
                    self.putpixel((i, j), WHITE)
                    continue

            box.sort()
            if len(box) == len(window_x):
                mid = box[int(len(box) / 2)]
                if mid == 1:
                    self.putpixel((i, j), BLACK)
                else:
                    self.putpixel((i, j), WHITE)
    # self.show()
    self.save("mov_noise_fig.jpg")
    return


def split_fig(self):
    frame = self.load()
    img_new = self.copy()
    frame_new = img_new.load()

    width, height = self.size
    line_status = None
    pos_x = []
    for x in range(width):
        pixs = []
        for y in range(height):
            pixs.append(frame[x, y])

        if len(set(pixs)) == 1:
            _line_status = 0
        else:
            _line_status = 1

        if _line_status != line_status:
            if _line_status != None:
                if _line_status == 0:
                    _x = x
                elif _line_status == 1:
                    _x = x - 1

                pos_x.append(_x)

                # 辅助线
                for _y in range(height):
                    frame_new[x, _y] = BLACK

        line_status = _line_status

    img_new.show()
    img_new.save("split_fig.jpg")

    i = 0
    divs = []
    boxs = []
    while True:
        try:
            x_i = pos_x[i]
            x_j = pos_x[i + 1]
        except:
            break

        i = i + 2
        boxs.append([x_i, x_j])

    fixed_boxs = []
    i = 0
    while i < len(boxs):
        box = boxs[i]
        if box[1] - box[0] < 10:
            try:
                box_next = boxs[i + 1]
                fixed_boxs.append([box[0], box_next[1]])
                i += 2
            except Exception:
                break
        else:
            fixed_boxs.append(box)
            i += 1

    for box in fixed_boxs:
        div = self.crop((box[0], 0, box[1], height))
        try:
            # divs.append(format_div(div,size=(20,40)))
            divs.append(div)
        except:
            divs.append(div)

    # 过滤掉非字符的切片
    _divs = []
    for div in divs:
        width, heigth = div.size
        if width < 5:
            continue

        frame = div.load()
        points = 0
        for i in range(width):
            for j in range(heigth):
                p = frame[i, j]
                if p == BLACK:
                    points += 1

        if points <= 5:
            continue

        # new_div = format_div(div)
        new_div = div
        _divs.append(new_div)
    return _divs


# def image_to_string(img, config='-psm 8'):
#     try:
#         result = pytesseract.image_to_string(img, lang='eng', config=config)
#         result = result.strip()
#         return result.lower()
#     except:
#         return None


# 测试代码
def main():
    img = Image.open("1.jpg")
    pre_concert(img)
    remove_noise(img, 2)
    img1 = split_fig(img)
    # image_to_string(img1,config='-psm 8')


if __name__ == '__main__':
    main()