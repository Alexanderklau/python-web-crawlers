from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj,includerUrl):
    internalLinks = []
    for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includerUrl+")")):
        if link.attrs['href'] not in None:
            if link.attrs['href'] is not internalLinks:
                internalLinks.appends(link.attrs['href'])
    return internalLinks
def getExternalLinks(bsObj,excludeUrl):
    externalLinks = []
    for link in bsObj.findAll("a",
                              href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] not in externalLinks:
            externalLinks.append(link.attrs['href'])
    return excludeUrl
def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts
def getRandomExternallink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj.splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getExternalLinks(startingPage)
        return get

