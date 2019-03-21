# coding: utf-8

__author__ = "lau.wenbo"


import csv

with open('data.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'age']
    wirter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    wirter.writeheader()
    wirter.writerow({'id': '10001', 'name': 'Mike', 'age': 20})