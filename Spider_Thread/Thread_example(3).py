import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def movie(func):
    for i in range(2):
        print("I wan listening to %s. %s" %(func,ctime()))
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'程序'))
threads.append(t1)
t2 = threading.Thread(target=movie,args=(u'编写'))
threads.append(t2)

if __name__ =="__main__":
    for t in threads:
        t.setDaemon(True)
        t.start()
    print("all over %s" %ctime())
