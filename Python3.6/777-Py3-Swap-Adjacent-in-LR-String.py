# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 21:17:30 2018

@author: hjiang
"""

"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", 
a move consists of either replacing one occurrence of "XL" with "LX", 
or replacing one occurrence of "RX" with "XR". 
Given the starting string start and the ending string end, return True if and 
only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Note:

1 <= len(start) = len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.
http://www.cnblogs.com/grandyang/p/9001474.html

L只能往前移动，因为是把 "XL" 变成 "LX"，同样，R只能往后移动，因为是把 "RX" 变成 "XR"。
我们观察这个test case，可以发现start中的R可以往后移动，没有问题，但是start中的L永远无法变到end中L的位置，
因为L只能往前移。这道题被归类为brainteaser，估计就是因为要观察出这个规律吧。
那么搞明白这个以后，我们其实可以用双指针来解题，
思路是，我们每次分别找到start和end中非X的字符，如果二者不相同的话，直接返回false，想想问什么？
这是因为不论是L还是R，其只能跟X交换位置，L和R之间是不能改变相对顺序的，
所以如果分别将start和end中所有的X去掉后的字符串不相等的话，那么就永远无法让start和end相等了。
这个判断完之后，就来验证L只能前移，R只能后移这个限制条件吧，当i指向start中的L时，那么j指向end中的L必须要在前面，
所以如果i小于j的话，就不对了，同理，当i指向start中的R，那么j指向end中的R必须在后面，所以i大于j就是错的，
最后别忘了i和j同时要自增1，不然死循环了，

"""

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        N = len(start)
        i, j = 0, 0
        while i < N and j < N:
            while i < N and start[i] == 'X':
                i += 1
            while j < N and end[j] == 'X':
                j += 1
            if (i < N) != (j < N):# "X"的数量要相等
                return False
            elif i < N and j < N: #当i指向start中的L时，那么j指向end中的L必须要在前面，指向start中的R，那么j指向end中的R必须在后面，
                if start[i] != end[j] or (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):# 第一个条件，去掉"X",必须相等
                    return False
            i += 1
            j += 1
        return True
    
#Time: (3n)
        
class Solution0:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        s = [(c, i) for i, c in enumerate(start) if c == 'L' or c == 'R']
        e = [(c, i) for i, c in enumerate(end) if c == 'L' or c == 'R']
        return len(s) == len(e) and all(c1 == c2 and (i1 >= i2 and c1 == 'L' or i1 <= i2 and c1 == 'R') \
            for (c1, i1), (c2, i2) in zip(s,e))
        
if __name__ == "__main__":
    print(Solution().canTransform("RXXLRXRXL","XRLXXRRLX"))
    
    
    
    
    
    
    
    
    
    