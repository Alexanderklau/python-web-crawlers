from urllib.request import urlopen,Request
import socket

def GetHtmlSource(url):
    try:
        htmSource = ""

        req = Request(url,headers={
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',})

        fb = urlopen(req,"")

        while 1:

            data = fb.read(1024)

            if not len(data):

                break

            htmSource += data

        fb.close()

        del fb

        del req

        htmSource = htmSource.encode('cp936')

        htmSource = format(htmSource)

        return htmSource

    except socket.error as err:

        str_err = "%s" % err

        return ""