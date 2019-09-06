# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:21:36 2018

@author: hjiang
"""

"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees 
(looked at upside down).

Write a function to count the total strobogrammatic numbers 
that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, 
the low and high numbers are represented as string.
https://github.com/tczhaodachuan/LeetCode/blob/24207cdb702486de6d0db7ed9d08ffb7683fe87d/src/main/google/StrobogrammaticNumber.py
http://www.cnblogs.com/grandyang/p/5203228.html

关键：一定要注意python和c++的区别: c++可以用&res来实现对于数字地址的调用，而python可以用dict等方式
"""
# Time:  O(n^2 * 5^(n/2))估计这里还需要乘一个k,因为还有点循环在里面
# Space: O(n)
class Solution(object):#自己写的，基本就是直接套用247的结果，然后过滤一下即可
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    # @param {integer} n
    # @return {string[]}
    def findStrobogrammatic(self, n):
        return self.findStrobogrammaticRecu(n, n)

    def findStrobogrammaticRecu(self, n, k):
        if k == 0:#偶数为空
            return ['']
        elif k == 1:#奇数为 0，1，8
            return ['0', '1', '8']

        result = []
        for num in self.findStrobogrammaticRecu(n, k - 2):
            for key, val in self.lookup.items():# 注意python 2.7 的iteritems()在python3中就是items()
                if n != k or key != '0':#这一句是亮点，因为只有n==k时，key!=0变成唯一向下的路，这就避免了010，000这种没有意义的数字
                    result.append(key + num + val)

        return result
    
    def strobogrammaticInRange(self, low, high):
        len_low = len(str(low))
        len_high = len(str(high))
        res = []
        for i in range(len_low, len_high + 1):
            res += self.findStrobogrammatic(i)
        res1 = []
        for num in res:
            if  int(low) <= int(num) <= int(high):
                res1.append(num)
        return len(res1)





# Time:  O(5^(n/2))
# Space: O(n)

class Solution0: #与solution1基本一样, 就看这个
    def strobogrammaticInRange(self, low, high):
#        count = {'count': 0, 'numbers': []}
        count = {'c':0} # 用dict传递
        # number grows from middle
        # odd digits number comes from '' string
        # even digits number comes from '1', '8' string, not '6','9' could be in the middle
        self.find(low, high, '', count)
        self.find(low, high, '0', count)
        self.find(low, high, '1', count)
        self.find(low, high, '8', count)
        return count["c"]

    def find(self, low, high, w, count):
        if len(str(low)) <= len(str(w)) <= len(str(high)):
#            if int(w) < int(low) or int(w) > int(high):
#                return
#            else:
#                if int(w) == 0 and len(str(w)) > 1:
#                    # avoid 0, 00, 0000
#                    return
            if str(int(w)) == w and int(low)<=int(w)<=int(high): # 如果不加这个， 将会出现010和080这种东西
                count['c'] += 1
#                count.append(1)
#                count['numbers'].append(w)
#                count['count'] += 1

        if len(str(w)) + 2 > len(str(high)):
            # if adding two edges will pass the length, return
            return
#        if len(str(w)) + 2 < len(str(high)):
            # if adding two edges won't pass the length, we can attach '0' on the sides
        self.find(low, high, '0' + w + '0', count)

        self.find(low, high, '1' + w + '1', count)
        self.find(low, high, '6' + w + '9', count)
        self.find(low, high, '9' + w + '6', count)
        self.find(low, high, '8' + w + '8', count)
        

        
class Solution1:
    def strobogrammaticInRange(self, low, high):
        count = {'count': 0, 'numbers': []}
#        count = {'c':0}
        # number grows from middle
        # odd digits number comes from '' string
        # even digits number comes from '1', '8' string, not '6','9' could be in the middle
        self.find(low, high, '', count)
        self.find(low, high, '0', count)
        self.find(low, high, '1', count)
        self.find(low, high, '8', count)
        return count['c']

    def find(self, low, high, w, count):
        if len(str(low)) <= len(str(w)) <= len(str(high)):
#            if int(w) < int(low) or int(w) > int(high):
#                return
#            else:
#                if int(w) == 0 and len(str(w)) > 1:
#                    # avoid 0, 00, 0000
#                    return
            if str(int(w)) == w and int(low)<=int(w)<=int(high): # 如果不加这个， 将会出现010和080这种东西
#                count['c'] += 1
                count['numbers'].append(w)
                count['count'] += 1

        if len(str(w)) + 2 > len(str(high)):
            # if adding two edges will pass the length, return
            return
#        if len(str(w)) + 2 < len(str(high)):
            # if adding two edges won't pass the length, we can attach '0' on the sides
        self.find(low, high, '0' + w + '0', count)

        self.find(low, high, '1' + w + '1', count)
        self.find(low, high, '6' + w + '9', count)
        self.find(low, high, '9' + w + '6', count)
        self.find(low, high, '8' + w + '8', count)
        
    
if __name__ == "__main__":
    print(Solution0().strobogrammaticInRange(50,100))
    print(Solution0().strobogrammaticInRange(50,100))
    