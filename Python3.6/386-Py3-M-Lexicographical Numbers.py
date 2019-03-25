# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:20:21 2019

@author: hjiang
"""

"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

https://blog.csdn.net/fuxuemingzhu/article/details/81776094

这个题的思路我是参考的Lexicographical Numbers 字典顺序的数字，不太好想。

如果curr乘以10小于等于n，那么下个数字应该是curr末尾补0；
如果curr已经到达了n，那么说明各位数字已经到头了，应该变化十位数字了，所以除以10，再加一。
这时可能会出现恰好进位的情况，而字典序可能是从末尾没有0的数字开始的，所以要把末尾的0去掉。
比如n=300时，会有这个队列1,10,100,101,102...198,199,2,20,200,201...299,3,30,300

代码如下：
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/81776094 
# Time:  O(n)
# Space: O(1)
"""
class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        cur = 1
        ans = []
        for i in range(n):
            ans.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10#也是操作十位，（这里出现的是30×10>=300的情况，开始操作31（顺序是3，30， 300， 31））
                cur += 1
                while cur % 10 == 0:#开始操作十位（最开始先操作各位）
                    cur //= 10
        return ans
    
if __name__ == "__main__":
    print(Solution().lexicalOrder(300))