# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests
import re
import pymysql
import json

class Craw:
    def get_html(self,url):
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        header = {'User-Agent':user_agent}
        bsobj = requests.get(url,headers = header)
        html = bsobj.text
        return html
    def getContent(self,reg,html):
        content = re.findall(reg,html,re.S)
        return content
    def seeting(self):
        DBKWARGS = {
            'db': 'Data_Store',
            'user': 'root',
            'passwd': '',
            'host': 'localhost',
            # 'port':3306,
            'use_unicode': True,
            'charset': 'utf8',
        }
        return DBKWARGS
    def connectDB(self):#
        DBKWARGS = self.seeting()
        db = pymysql.connect(**DBKWARGS)
        # db = pymysql.connect(host,dbName,user,password,charset,port)
        # return db
        cursorDB = db.cursor()
        return cursorDB
    def creatTable(self,createTableName):
        createTableSql = "CREATE TABLE IF NOT EXISTS " + createTableName + "(Movie VARCHAR(100),star VARCHAR(40))"
        DB_create = self.connectDB()
        # cursor_create = DB_create.cursor()
        # cursor_create.execute(createTableSql)
        # DB_create.close()
        DB_create.execute(createTableSql)
        DB_create.close()
        print('creat table ' + createTableName + ' successfully')
        return createTableName

    def inserttable(self,insertTable,insertMovie, insertStar):
        insertContentSql = "INSERT INTO " + insertTable +"(Movie,Star)VALUES(%s,%s)"
                # insertContentSql="INSERT INTO "+insertTable+"(time,title,text,clicks)VALUES("+insertTime+" , "+insertTitle+" , "+insertText+" , "+insertClicks+")"
        DB_insert = self.connectDB()
        # cursor_insert = DB_insert.cursor()
        # cursor_insert.execute(insertContentSql, (insertMovie, insertStar))
        DB_insert.execute(insertContentSql,(insertMovie,insertStar))
        # DB_insert.commit()
        DB_insert.close()
        print('inert contents to '+ insertTable +' successfully')

url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=rank&page_limit=20&page_start=20"

reg_star = r'"title":"(.*?)"'
reg_movie = r'"rate":"(.*?)"'
craw = Craw()
html = craw.get_html(url)
stars = craw.getContent(reg_star,html)
movies = craw.getContent(reg_movie,html)
for star,movie in zip(stars,movies):
    Star = star
    Movie = movie
    c = craw.creatTable('lwb')
    craw.inserttable(c,Movie,Star)



            # if __name__ == '__main__':