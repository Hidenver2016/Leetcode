# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:20:13 2018

@author: hjiang
"""

"""
There is a box protected by a password. The password is n digits, 
where each letter can be one of the first k digits 0, 1, ..., k-1.

You can keep inputting the password, the password will automatically be matched against the last n digits entered.

For example, assuming the password is "345", I can open it when I type "012345", 
but I enter a total of 6 digits.

Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.

Example 1:
Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:
Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
Note:
n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096.

"""
# Time:  O(n * k^n)
# Space: O(n * k^n)
class Solution(object):
    def crackSafe(self, n, k):# n是长度， k是种类
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = "0" * (n - 1)
        visits = set() #类似于dp,做记录的
        for x in range(k ** n):
            current = ans[-n+1:] if n > 1 else '' # ans[-n+1:] 正好是 n-1个数，
            for y in range(k - 1, -1, -1):
                if current + str(y) not in visits: #加上一个y,正好是长度为n的序列
                    visits.add(current + str(y))
                    ans += str(y)
                    break
        return ans

if __name__ == "__main__":
    print(Solution().crackSafe(2,2))
    
    
    