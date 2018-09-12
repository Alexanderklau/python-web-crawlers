from time import ctime, sleep
from threading import Thread


def loop0():
    print('start loop 0 at :', ctime())
    sleep(4)
    print('loop 0 at :', ctime())


def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())


def main():
    print('starting at:', ctime())
    t1 = Thread(target=loop0, name='loop0')
    t2 = Thread(target=loop1, name='loop1')

    t1.start()
    t2.start()
    print('all done at:', ctime())


if __name__ == '__main__':
    main() 