# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:11:22 2018

@author: hjiang
time O(n)
space O(k)

可否在一未知大小的集合中，随机取出一元素？
当内存无法加载全部数据时，如何从包含未知大小的数据流中随机选取k个数据，并且要保证每个数据被抽取到的概率相等。

一共取k个数，前面k个全部保留，后面的就要以概率来替换


1. 对于前k个数，我们全部保留

2. 对于第i（i>k）个数，我们以 k/i 的概率保留第i个数，并以 1/k 的概率与前面已选择的k个数中的任意一个替换。
"""

import random
def random_subset(iterator, K): # iterator is a stream 
    result = []
    N = 0

    for item in iterator:
        N += 1 # N就是当前数的长度
        if len( result ) < K:
            result.append( item ) #前面的都是等概率的
        else:
#            s = int(random.random() * N)#产生一个随机0～N的数
            s = random.randrange(0, N)
            if s < K:#以 k/i 的概率保留第i个数
                result[ s ] = item#替换, 并以 1/k 的概率与前面已选择的k个数中的任意一个替换。

    return result

if __name__ == "__main__":
    iterator = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; 
    K = 5
    print(random_subset(iterator, K))