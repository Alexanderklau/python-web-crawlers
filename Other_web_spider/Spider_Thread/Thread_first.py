import threading
import time
import random


# 继承threading.Thread，并重载run函数。

class jdThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
        self.create_time = time.time()
        self.local = threading.local()
        # local具有全局访问权，主线程，子线程都能访问它，但是它的值却是各当前线程有关,
        # 如果想在当前线程保存一个全局值，并且各自线程互不干扰，使用local类,实际它是一个字典

    def run(self):
        self.local = []
        time.sleep(1)
        print("线程", self.num, "被创建")

        for i in range(8):
            self.local.append(random.randrange(10))
        # 显示线程的状态，和随机产生的10个数字
        print(threading.currentThread(), self.local)

        print(time.time() - self.create_time)

        print("线程", self.num, "结束")
        print("\n")


print("主线程开始")
for item in range(7):
    t = jdThread(item)
    t.start()
    # join函数控制线程执行顺序，不要在start之前调用join函数
    # t.join()
    # isDaemon函数查看线程后台运行状态
    # print(t.isDaemon())
print("主线程结束")