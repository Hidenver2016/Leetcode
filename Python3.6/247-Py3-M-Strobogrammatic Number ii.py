# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:03:39 2019

@author: hjiang
"""

"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""
# Time:  O(n^2 * 5^(n/2))
# Space: O(n)
#http://www.cnblogs.com/grandyang/p/5200919.html
#注意好关系，这个每次都是和上一次的答案差两位数，所以迭代就是n-2

class Solution(object):
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

if __name__ == "__main__":
    print(Solution().findStrobogrammatic(4))
    
    
class Solution1:#原来提交过的答案:

    def findStrobogrammatic(self, n):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        def helper(m,n):
            if m == 0:
                return []
            if m == 1:
                return ["0", "1", "8"]
            
            tmp = helper(m-2,n)
            res = []
            if not tmp:
                res.append("11")
                res.append("88")
                res.append("69")
                res.append("96")
                if m != n:
                    res.append("00")
                    
            for t in tmp:
                res.append("1" + t + "1")
                res.append("9" + t + "6")
                res.append("8" + t + "8")
                res.append("6" + t + "9")
                if m != n:
                    res.append("0" + t + "0")
            return res       
        return helper(n,n)