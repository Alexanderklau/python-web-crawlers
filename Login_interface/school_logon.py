from urllib.request import *
from urllib.parse import *
import re
import http.cookiejar
import time

CaptchaUrl = "http://210.41.224.117/Login/xLogin/yzmDvCode.asp"
PostUrl = "http://210.41.224.117/Login/xLogin/Login.asp"
# 验证码地址和post地址
cookie = http.cookiejar.CookieJar()
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
# 将cookies绑定到一个opener cookie由cookielib自动管理
username = '2012214001'
password = 'Lw136899'
# 用户名和密码
picture = opener.open(CaptchaUrl).read()
# 用openr访问验证码地址,获取cookie
local = open('image.jpg', 'wb')
local.write(picture)
local.close()
# 保存验证码到本地
SecretCode = input('输入验证码： ')
# 打开保存的验证码图片 输入
postData = {
    'WinW':'1920',
    'Winh':'1018',
    'txtld':username,
    'txtMM':password,
    'verifycode':SecretCode,
    'codeKey':


}
# 根据抓包信息 构造表单
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
}
# 根据抓包信息 构造headers
data = urlencode(postData)
# 生成post数据 ?key1=value1&key2=value2的形式
request = Request(PostUrl, data, headers)
# 构造request请求
try:
    response = opener.open(request)
    result = response.read().decode('gb2312')
    print (result)
except HTTPError as e:
    print(e.code)
