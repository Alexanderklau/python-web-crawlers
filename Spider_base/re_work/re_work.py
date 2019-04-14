# coding: utf-8

__author__ = "lau.wenbo"


import re

string = """
                <dd>
                        <i class="board-index board-index-3">3</i>
    <a href="/films/2641" title="罗马假日" class="image-link" data-act="boarditem-click" data-val="{movieId:2641}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/289f98ceaa8a0ae737d3dc01cd05ab052213631.jpg@160w_220h_1e_1c" alt="罗马假日" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/2641" title="罗马假日" data-act="boarditem-click" data-val="{movieId:2641}">罗马假日</a></p>
        <p class="star">
                主演：格利高里·派克,奥黛丽·赫本,埃迪·艾伯特
        </p>
<p class="releasetime">上映时间：1953-09-02(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
"""
res = '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a' \
      '+ '''
pattern = re.compile(res, re.S)
print(pattern)
text = re.findall(pattern, string)
print(text)
