import requests
from bs4 import BeautifulSoup
import re
import urllib.request

loginUrl = 'https://accounts.douban.com/login'

formData = {
    'redir':'##########',
    'source':None,
    'login':u'登录',
    'form_email':'###########',
    'form_password':'#########'
}
headers = {
    "User-Agent":'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}
r = requests.post(loginUrl,data=formData,headers=headers)
page = r.text
soup = BeautifulSoup(page, "html.parser")
captchaAddr = soup.find('img', id='captcha_image')['src']
# 利用正则表达式获取captcha的ID
reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
captchaID = re.findall(reCaptchaID, page)
# print captchaID
# 保存到本地
urllib.request.urlretrieve(captchaAddr, "captcha.jpg")
captcha = input('please input the captcha:')
formData['captcha-solution'] = captcha
formData['captcha-id'] = captchaID
r = requests.post(loginUrl,data=formData,headers=headers)
print(r)
