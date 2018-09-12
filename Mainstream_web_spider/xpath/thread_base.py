# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import threading
import time
import random

def worker_func():
    print('Work thread is started at %s' % threading.current_thread(),time.ctime())
    random.seed()
    time.sleep(random.random())
    print('Work thread is finished at %s' % threading.current_thread(),time.ctime())

def simple_therad_demo():
    for i in range(10):
        threading.Thread(target=worker_func()).start()
def work_lock(lock):
    lock.acquire()
    worker_func()
    lock.release()
gLock = threading.Lock()
gSem = threading.Semaphore(5)
def thread_demo_lock():
    for i in range(20):
        threading.Thread(target=work_lock,args=[gSem]).start()


if __name__ == '__main__':
    thread_demo_lock()
    # simple_therad_demo()