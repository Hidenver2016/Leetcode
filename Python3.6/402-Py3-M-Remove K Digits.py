# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 22:59:43 2019

@author: hjiang
"""

"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0. 


https://blog.csdn.net/fuxuemingzhu/article/details/81034522
https://www.cnblogs.com/grandyang/p/5883736.html

实际上这里利用到了单调栈的思想，可以参见博主之前的一篇总结帖 LeetCode Monotonous Stack Summary 单调栈小结。
这里我们维护一个递增栈，只要发现当前的数字小于栈顶元素的话，就将栈顶元素移除，比如点那个遍历到2的时候，栈里面有1和3，
此时2小于栈顶元素3，那么将3移除即可。为何一定要移除栈顶元素呢，后面说不定有更大的数字呢？
这是因为此时栈顶元素在高位上，就算后面的数字再大，也是在低位上，我们只有将高位上的数字尽可能的变小，才能使整个剩下的数字尽可能的小。


int("002302") 就是 2302
"""
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return '0'
        stack = []
        for n in num:
            while stack and k and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        while k:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        return str(int("".join(stack)))
    
print(Solution().removeKdigits("1432219", 3))
    
    