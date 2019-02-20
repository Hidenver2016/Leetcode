# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:51:12 2019

@author: hjiang
"""

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
    (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:
            01234567890123  
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N  0,6,12
A   L S  I G  1,5,7,11,13
Y A   H R
P     I
明眼人一看就知道，这个肯定是有公式的。我自己推导的公式和JustDoIT的一样：

(1)第一行和最后一行下标间隔都是interval = n*2-2;

(2)中间行的间隔是周期性的,第i行的间隔是: interval–2*i, 2*i, interval–2*i, 2*i, interval–2*i, 2*i, …

代码如下：
--------------------- 
作者：负雪明烛 
来源：CSDN 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/80830509 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
# Time:  O(n)
# Space: O(n)

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        ans = ""
        interval = 2 * (numRows - 1)
        for i in range(0, len(s), interval):#第0行
            ans += s[i]
        for row in range(1, numRows - 1):
            inter = 2 * row
            i = row
            while i < len(s):
                ans += s[i]
                inter = interval - inter# interval-2*i; interval-(interval-2*i); ...
                i += inter
        for i in range(numRows - 1, len(s), interval):#最后一行
            ans += s[i]
        return ans