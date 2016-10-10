from urllib import parse,request
from bs4 import BeautifulSoup as BS
import json
import datetime
import xlsxwriter

starttime = datetime.datetime.now()

url = r'http://www.jiu-tuo.com/list-jiutuo--1'
tag = ['']