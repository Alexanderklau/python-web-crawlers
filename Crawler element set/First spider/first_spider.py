from urllib.request import *

def download(url):
    print('Downloading:',url)
    try:
        html = urlopen(url).read()
    except URLError as err:
        print('Download error',e.reason)
        html = None
    return html


