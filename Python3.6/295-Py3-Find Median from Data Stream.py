# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:26:27 2019

@author: hjiang
"""

"""
Median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
"""

# Time:  O(nlogn) for total n addNums, O(logn) per addNum, O(1) per findMedian.
# Space: O(n), total space
"""
http://www.cnblogs.com/grandyang/p/4896673.htmlfind
C++ 默认是最大堆，正好是个反的
这里用到的解法十分巧妙，我们使用大小堆来解决问题，其中大堆保存右半段较大的数字，小堆保存左半段较小的数组。
这样整个数组就被中间分为两段了，由于堆的保存方式是由大到小，我们希望大堆里面的数据是从小到大，
这样取第一个来计算中位数方便。我们用到一个小技巧，就是存到大堆里的数先取反再存，
这样由大到小存下来的顺序就是实际上我们想要的从小到大的顺序。当大堆和小堆中的数字一样多时，
我们取出大堆小堆的首元素求平均值，当小堆元素多时，取小堆首元素为中位数，

heapq默认是最小堆，
heapq.heappush(heap, a) O(logn)：先加入，然后在向上冒泡
heapq.heappop(heap) O(logn)： 先弹出，然后把最后的数放在第一个，向下sink
heapq.heappushpop(heap,a):先弹出，然后把a放在第一个，向下sink
heap
"""

#from heapq import heappush, heappop

import heapq
class MedianFinder1:
    def __init__(self):
        self.small = []  # 想搞成最大堆，就全部压负数进去
        self.large = []  # the larger half of the list, min heap
    
    def addNum(self, num):
        if len(self.small) == len(self.large):#长度相等时，self.small把最大数弹出来，把新数压入。self.large接收self.small的最大值 
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
#            print "self.large1", self.large
#            print "self.small1", self.small
        else:#长度不等时，self.large把最小数弹出，压入新数。self.small接收self.large的最小数，然后加负号压入
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
#            print "self.large2", self.large
#            print "self.small2", self.small
    
    def findMedian(self):
        if len(self.small) == len(self.large):
#            print "self.large3", self.large
#            print "self.small3", self.small
#            print "self.large[0], self.small[0]", self.large[0], self.small[0]
            return float(self.large[0] - self.small[0]) / 2.0
        else:
#            print "self.large4", self.large
#            print "self.small4", self.small
            return float(self.large[0])

if __name__ == "__main__":
    mf = MedianFinder1()
    mf.addNum(-1)
    mf.addNum(-2)
    mf.addNum(-3)
    mf.addNum(-4)
#    mf.addNum(5)
    print (mf.findMedian())
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               