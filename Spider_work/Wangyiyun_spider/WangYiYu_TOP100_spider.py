# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
import re
import time
class WY_Music:
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent':self.user_agent}
    def WY_TOP(self):
        html = requests.get('http://music.163.com/discover/toplist',headers = self.headers)
        html.encoding = 'urf-8'
        titles = re.findall('<li><a href="/song\?id=.*?">(.*?)</a></li>',html.text)
        artiles = re.findall('"artists":\[\{.*?,"name":"(.*?)",.*?}]',html.text)
        TOPs = [x for x in range(1,101)]
        MC_HP = re.findall('<li><a href="(/song\?id=.*?)">.*?</a></li>',html.text)
        # http://music.163.com/#/song?id=466794193
        for TOP,title,artile,mc_hp in zip(TOPs,titles,artiles,MC_HP):
            data = {
                '排名':TOP,
                '歌名':title,
                '歌手':artile,
                '歌曲页': 'http://music.163.com/#' + mc_hp,
                '更新时间':time.strftime('%Y-%m-%d',time.localtime(time.time()))
            }
            print(data)
c = WY_Music()
c.WY_TOP()
# if __name__ == '__main__':