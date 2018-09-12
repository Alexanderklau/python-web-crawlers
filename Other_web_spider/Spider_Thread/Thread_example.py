from threading import Thread
import threading
from time import sleep,ctime
import _thread

def loop0():
    print('Start loop 0 at:',ctime())
    sleep(4)
    print('loop 0 done at:',ctime())

def loop1():
    print('start loop 1 at:',ctime())
    sleep(2)
    print('loop 1 done at:',ctime())

def main():
    print('starting at:',ctime())
    # _thread.start_new_thread(loop1(),())
    # _thread.start_new_thread(loop0(),())
    threading._start_new_thread(loop0(),())
    threading._start_new_thread(loop1(),())
    sleep(6)
    print('all Done at:',ctime())

if __name__ == '__main__':
    main()