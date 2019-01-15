# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:04:56 2019

@author: hjiang
"""

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

https://blog.csdn.net/fuxuemingzhu/article/details/79515180
"""

"""
这个题要找到组合，组合和排列的不同之处在于组合的数字出现是没有顺序意义的。

剑指offer的做法是找出n个数字中m的数字的组合方法是，把n个数字分成两部分：
第一个字符和其他的字符。如果组合中包括第一个字符，那么就在其余字符中找到m-1个组合；
如果组合中不包括第一个字符，那么就在其余字符中找到m个字符。所以变成了递归的子问题。

我的做法如下，这个之中用到了if k > len(array)的做法，防止数组过界陷入死循环（其作用主要是对第二个递归而言的）
"""
#方法一：递归
class Solution(object):#这个感觉比较难理解
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(range(1, n + 1), k, res, [])
        return res
    
    def helper(self, array, k, res, path):
        if k > len(array):
            return
        if k == 0:
            res.append(path)
        else:
            self.helper(array[1:], k - 1, res, path + [array[0]])#在k-1中找剩下的
            self.helper(array[1:], k, res, path)# 在其余的中找剩下的
            
            
"""
方法二：回溯法 #这个比较好理解
这样的思想是我们抽取第一个字符，然后从后面n-1个字符中抽出m-1个；抽取第二个字符，
再从后面的n-2个字符抽出m-1个……这样循环下去。因为这样的操作每次都是往后进行寻找的，所以不用考虑去重的问题。
"""
# Time:  O(k * C(n, k))
# Space: O(k)            
class Solution1(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(range(1, n + 1), k, res, [])
        return res
    
    def helper(self, array, k, res, path):
        if k > len(array):
            return
        if k == 0:
            res.append(path)
        else:
            for i in range(len(array)):
                self.helper(array[i + 1:], k - 1, res, path + [array[i]])            
            
if __name__ == "__main__":
    print(Solution().combine(4,2))
    
    
    
    
    
    
    
    
    
    