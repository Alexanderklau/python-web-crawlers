import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print("I was at the %s. %s" %(func,ctime()))
        sleep(1)

def movie(func):
    for i in range(2):
        print("I was at the %s. %s" %(func,ctime()))
        sleep(5)

if __name__ == "__main__":
    music(u'程序')
    movie(u'编写')

    print("all over %s" %ctime())