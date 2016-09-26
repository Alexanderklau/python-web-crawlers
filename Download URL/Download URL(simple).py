import urllib2
def download(url):
    print 'Downloading:',url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:',e.reason
        html = None
    return html
