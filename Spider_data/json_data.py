# coding: utf-8

__author__ = "lau.wenbo"


import json


data = [{
    'name': 'bob',
    'gender': 'male',
    'birthday': '1992-01-18'
}]
with open('data.json', 'w') as file:
    file.write(json.dumps(data))