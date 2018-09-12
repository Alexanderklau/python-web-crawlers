from time import ctime,sleep

def music():
    for i in range(2):
        print("I was listening to music.")
        sleep(1)

def movie():
    for i in range(2):
        print("I was at the movies.")
        sleep(5)

if __name__ == '__main__':
    music()
    movie()
    print('all over %s' %ctime())

