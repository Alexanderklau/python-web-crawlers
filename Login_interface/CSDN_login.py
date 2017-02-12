# python3.3 可以登录成功  
import urllib.parse, urllib.request, http.cookiejar, re
import tools
from Login_interface.log import log

cookie = http.cookiejar.CookieJar()
cookieProc = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookieProc)
h = opener.open('https://passport.csdn.net').read().decode("utf8")
patten1 = re.compile(r'name="lt" value="(.*?)"')
patten2 = re.compile(r'name="execution" value="(.*?)"')
b1 = patten1.search(h)
b2 = patten2.search(h)
postData = {
    'username': 'csdn用户名',
    'password': 'csdn密码',
    'lt': b1.group(1),
    'execution': b2.group(1),
    '_eventId': 'submit',
}

postData = urllib.parse.urlencode(postData).encode(encoding='UTF8')

opener.addheaders = [('Origin', 'https://passport.csdn.net'),
                     ('User-Agent',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'),
                     ('Referer', 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn')
                     ]
response = opener.open('https://passport.csdn.net', data=postData)
text = response.read().decode('utf-8', 'ignore')
# print(text)  
# exit()  
tools.logs(text, 'csdn_login.html')

response2 = opener.open('http://my.csdn.net/my/mycsdn')
text2 = response2.read().decode('utf-8', 'ignore')
tools.logs(text2, 'csdn_mycsdn.html')
