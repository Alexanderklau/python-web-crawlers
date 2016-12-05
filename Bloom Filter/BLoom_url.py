# encoding=UTF-8
'''''
Created on 2014年6月21日

@author: jin
'''
import BitVector

import functools


class MyHash():  # 哈希类，根据不同参数初始化后作为不同的哈希函数

    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):  # 计算哈希值得过程
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])  # ord()函数计算传入的url字符串中每一个字符在ASCII码表中对应的顺序值
        return (self.cap - 1) & ret  # 返回哈希值，即在比特序列中的位置


class BloomFilter():
    def __init__(self, BIT_SIZE=1 << 31):
        self.BIT_SIZE = 1 << 31  # 不拢过滤器的比特数,
        self.seeds = [5, 7, 11, 13, 19, 31, 37, 61]  # 8个种子，用于产生hash函数
        self.bitset = BitVector.BitVector(size=self.BIT_SIZE)
        self.hashFuncList = []
        for i in range(len(self.seeds)):
            self.hashFuncList.append(MyHash(self.BIT_SIZE, self.seeds[i]))  # 对每个种子，创建一个MyHash对象，一共8个

    def insert(self, value):  # 插入值，这里并非真正地插入并存储，而是把该值对应的8个位置的比特位置为1
        for function in self.hashFuncList:
            locationBit = function.hash(value)  # 计算应该置为1的比特位
            self.bitset[locationBit] = 1

    def isContaions(self, value):
        if value == None:
            return False
        ret = True
        for f in self.hashFuncList:
            locationBit = f.hash(value)
            ret = ret & self.bitset[locationBit]  # 可以看出，对8个哈希函数，只要有一个为0，那么将返回0，即该值尚未存在
        return ret


def Main():  # 主函数

    fd = open("urls.txt")  # 有重复的网址 http://www.kalsey.com/tools/buttonmaker/
    bloomfilter = BloomFilter()
    while True:
        url = fd.readline()
        if functools.cmp_to_key(url, 'exit') == 0:
            print('complete and exit now')
            break
        elif bloomfilter.isContaions(url) == False:
            bloomfilter.insert(url)
        else:
            print('url :%s has exist' % url)


Main()