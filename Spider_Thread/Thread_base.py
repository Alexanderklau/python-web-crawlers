# coding=utf-8
import threading  # 导入threading包
from time import sleep
import time


def task1():
    print("Task 1 executed.")
    sleep(1)


def task2():
    print("Task 2 executed.")
    sleep(5)


print("多线程：")
starttime = time.time()  # 记录开始时间
threads = []  # 创建一个线程列表，用于存放需要执行的子线程
t1 = threading.Thread(target=task1)  # 创建第一个子线程，子线程的任务是调用task1函数，注意函数名后不能有（）
threads.append(t1)  # 将这个子线程添加到线程列表中
t2 = threading.Thread(target=task2)  # 创建第二个子线程
threads.append(t2)  # 将这个子线程添加到线程列表中

for t in threads:  # 遍历线程列表
    t.setDaemon(True)  # 将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
    t.start()  # 启动子线程
endtime = time.time() # 记录程序结束时间
totaltime = endtime - starttime # 计算程序执行耗时
print("耗时：{0:.5f}秒".format(totaltime)) # 格式输出耗时
print('---------------------------')

# 以下为普通的单线程执行过程，不需解释
print("单线程：")
starttime = time.time()
task1()
task2()
endtime = time.time()
totaltime = endtime - starttime
print("耗时：{0:.5f}秒".format(totaltime))