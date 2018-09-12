# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import pymysql
# conn = pymysql.connect(host='127.0.0.1',user='root',passwd=None,db='xici_IP')
# cur = conn.cursor()
# cur.execute("drop table if exists student")
# #删除原有的表student
# cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
# #建立一个新表student，字段为id,name,class,age
# cur.execute("insert into student values('1','Tom','3 year 2 class','9')")
# #往表里添加数据
# cur.execute("delete from student where age='9'")
# #删除选定的数据
conn = pymysql.connect(host='127.0.0.1',user='root',passwd=None,db='xici_IP')
cur = conn.cursor()
cur.execute("drop table if exists IP")
# cur.execute("create table IP(address varchar(255),Port varchar(30),Location varchar(10))")
# sqli="insert into IP values(%s,%s,%s)"
# cur.execute(sqli,(1,2,3))
cur.execute("CREATE TABLE IF NOT EXISTS `IP` (`IP` varchar(255) NOT NULL DEFAULT '',\
  `PORT` varchar(255) NOT NULL DEFAULT '',\
  `TYPE` varchar(255) DEFAULT NULL,\
  `GET_POST` varchar(255) DEFAULT NULL,\
  `POSITION` varchar(255) DEFAULT NULL,\
  `SPEED` varchar(255) DEFAULT NULL,\
  `LAST_CHECK_TIME` varchar(255) DEFAULT NULL,\
  PRIMARY KEY (`IP`,`PORT`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
sqli="insert into IP values(%s,%s,%s)"
cur.execute())
cur.close()
conn.commit()
conn.close()






# if __name__ == '__main__':