#-*-coding:gb2312-*-
import requests
parms = {'txtld':'2012214001',
         'txtMM':'Lw136899'}
r = requests.post("http://210.41.224.117/Login/xLogin/Login.asp",data=parms)
print(r.text)