# coding : utf-8

from io import BytesIO
import pycurl


def writefile(fstr,xfilename):
    f = open(xfilename,'w')
    f.write(fstr)
    f.close()

html = BytesIO
c = pycurl.Curl()

myUrl = 'http://www.cuit.com'

c.setopt(pycurl.URL,myUrl)

c.setopt(pycurl.WRITEFUNCTION,html.write)

c.setopt(pycurl.FOLLOWLOCATION,1)

c.setopt(pycurl.MAXREDIRS,5)

c.setopt(pycurl.CONNECTTIMEOUT,60)

c.setopt(pycurl.TIMEOUT,300)

c.setopt(pycurl.USERAGENT,"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko")

c.perform()

print(c.getinfo(pycurl.HTTP_CODE))

print(html.getvalue().decode('utf-8'))

writefile(html.getvalue().decode('utf-8'),"down.txt")
