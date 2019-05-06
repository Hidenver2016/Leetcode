# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:01:54 2019

@author: hjiang
"""

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

https://blog.csdn.net/fuxuemingzhu/article/details/80657420
只要看到所有的组合，一般都是用回溯
"""

# Time:  O(n^m) = O(3^4)
# Space: O(n * m) = O(3 * 4)

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:#是不是能满足在最多4个3位数字组成, 不写也没关系，就是慢一点
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))#注意 '.'join(path)
            return
        for i in range(min(3, len(s))):#这个最多就是3
            cur = s[:i+1]
            if (cur[0] == '0' and len(cur) >= 2) or int(cur) > 255:break# 不符合条件，直接跳出
            self.dfs(s[i+1:], path + [cur], res)#path是一段段的往后搜索