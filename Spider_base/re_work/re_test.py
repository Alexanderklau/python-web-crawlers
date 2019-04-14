# coding: utf-8

__author__ = "lau.wenbo"


import re

class retext:

    def __init__(self):
        self.file = './resule.txt'

    def get_data(self):
        f = open(self.file, 'r')
        data = f.read()
        return data

    def clear_data(self, data):
        pattern = re.compile(
            '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
            re.S)
        items = re.findall(pattern, data)
        for item in items:
            yield {
                'index': item[0],
                'image': item[1],
                'title': item[2].strip(),
                'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
                'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
                'score': item[5].strip() + item[6].strip()
            }


if __name__ == '__main__':
    z = retext()
    data = z.get_data()
    for x in z.clear_data(data):
        print(x)
