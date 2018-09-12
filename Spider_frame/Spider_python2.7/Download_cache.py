import urllib2
class Downloader:
    def __init__(self,delay=5,user_agent='wswp',proxies=None,
                 num_retries=1,cache=None):
        self.throttle = Throttle(delay)
