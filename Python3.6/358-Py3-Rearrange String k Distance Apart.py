# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:54:28 2019

@author: hjiang
"""

"""
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
https://blog.csdn.net/fuxuemingzhu/article/details/83039098
使用Counter统计每个字符出现的次数，然后使用大根堆，每次弹出出现次数最多的字符，添加到生成结果字符串的末尾。
如果剩余的不同字符个数不够k，那么说明不能满足题目的要求，返回空字符串。
另外，每次弹出出现次数最多的字符之后，不能直接放入堆中，因为直接放入堆中可能下次又被弹出来，
所以应该放入一个临时的数组中，在单次操作结束之后再重新插入堆中。

时间复杂度是O(N)，空间复杂度是O(N)。

"""
#https://leetcode.com/problems/rearrange-string-k-distance-apart/discuss/83198/20-line-linear-time-Python-solution
import collections
import heapq
class Solution(object):#看这个
    def rearrangeString(self, str, k):
        heap = [(-freq, char) for char, freq in collections.Counter(str).items()]
        heapq.heapify(heap) #[(-3, 'a'), (-2, 'c'), (-2, 'b'), (-1, 'd')]  输入"aaadbbcc",3为例
        res = []
        while len(res) < len(str):
            if not heap: return ""
            freq, char = heapq.heappop(heap)
            stack = []
            res.append(char)
            for j in range(k - 1):#这个地方就表示写入顺序，同时也表示最远距离小于k,对于同一个字母
                if len(res) == len(str): return "".join(res)
                if not heap: return ""
                fre, nex = heapq.heappop(heap)
                res.append(nex)
                if fre < -1: #fre都是负数，下面一行+1就表示用掉了一次
                    stack.append((fre+1, nex))#stack中间也是出现次数多的在前面，少的在后面， 
            while stack:
                heapq.heappush(heap, stack.pop())#把用掉的又重新写进去
            heapq.heappush(heap, (freq+1, char))#把最先弹出来的也要重新写进去
        return "".join(res)

    
    
    
if __name__ == "__main__":
    print(Solution().rearrangeString("aaadbbcc",3))    
    
    
    
    
    
    
    
    
    
