import BeautifulSoup
import urllib2
def download(url):
    return urllib2.urlopen(url).read()

url = "https://www.zhihu.com/people/yemilice"
html = download(url)
soup = BeautifulSoup(html)
tr = soup.find(attrs={'id':'zh-profile-answers-inner-list'})
td = tr.find({'class':'zm-profile-question'})
area = td.text
print area