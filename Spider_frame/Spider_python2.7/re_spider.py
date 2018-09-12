import urllib2
import re

def download(url):
    return urllib2.urlopen(url).read()


url = 'https://www.zhihu.com'
html = download(url)
re.findall('<h2 class="zm-profile-question".*?>(.*?)</h2>',html)
