from urllib.request import urlopen,urlretrieve,Request
from urllib.parse import urlencode
Login_Url = 'https://www.zhihu.com/login/email'
Login_EMAIL = 'example'
Login_PASSWORD = 'example'
data = {
    'email':Login_EMAIL,
    'password':Login_PASSWORD,
}
encoded_Data = urlencode(data)
request = Request(Login_Url,encoded_Data)
response = urlopen(request)
response.getUrl()
