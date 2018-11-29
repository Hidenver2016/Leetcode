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

关键：一定要注意python和c++的区别: c++可以用&res来实现对于数字地址的调用，而python可以用dict等方式
"""

class Solution0:
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
    print(Solution0().strobogrammaticInRange(0,1680))
    print(Solution0().strobogrammaticInRange(50,100))
    