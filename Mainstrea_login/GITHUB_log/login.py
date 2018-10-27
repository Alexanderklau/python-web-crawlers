# coding: utf-8
__author__ = 'lau.wenbo'


import requests
import re

login_url  = 'https://github.com/login'
user = 'xxxxxxxxxxxx'
password  = 'xxxxxxxxxxxxxx'
user_headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}

session  = requests.Session()
response = session.get(login_url, headers = user_headers)
pattern = re.compile(r'<input name="authenticity_token" type="hidden" value="(.*)" />')

authenticity_token = pattern.findall(response.content)[0]

login_data = {
    'commit' : 'Sign in',
    'utf8' : '%E2%9C%93',
    'authenticity_token' : authenticity_token,'login' : user,
    'password' : password
}

session_url  = 'https://github.com/session'
response = session.post(session_url, headers = user_headers, data = login_data)