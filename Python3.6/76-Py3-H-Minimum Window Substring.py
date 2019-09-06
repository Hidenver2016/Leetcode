# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:32:53 2019

@author: hjiang
"""

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
The current window is s[i:j] and the result window is s[I:J]. 
In need[c] I store how many times I need character c (can be negative) and 
missing tells how many characters are still missing. In the loop, first add the new character to the window. 
then, if nothing is missing, remove as much as possible from the window start and then update the result.

https://www.cnblogs.com/grandyang/p/4340948.html
先扩展，再收缩，就好像一个窗口一样，先扩大右边界，然后再收缩左边界，上面的例子中我们是右边界无法扩大了后才开始收缩左边界，
实际上对于复杂的例子，有可能是扩大右边界，然后缩小一下左边界，然后再扩大右边界等等。这就很像一个不停滑动的窗口了，
这就是大名鼎鼎的滑动窗口Sliding Window了.做法如下：

- 我们最开始先扫描一遍T，把对应的字符及其出现的次数存到HashMap中。

- 然后开始遍历S，就把遍历到的字母对应的HashMap中的value减一，如果减1后仍大于等于0，cnt自增1。

- 如果cnt等于T串长度时，开始循环，纪录一个字串并更新最小字串值。然后将子窗口的左边界向右移，
如果某个移除掉的字母是T串中不可缺少的字母，那么cnt自减1，表示此时T串并没有完全匹配。

此题中need 表示一个hashtable，记录字母的数字，如果为负数的话，证明当前区间里面有多于要求的字母，即字母数大于t中的对应字母数，可以缩小空间

"""
import collections
class Solution:
    def minWindow(self, s, t):#看这个，需要牢记！！！
        need, missing = collections.Counter(t), len(t)# need Counter({'A': 1, 'B': 1, 'C': 1})
        i = Start = End = 0
        for j, c in enumerate(s, 1):
#            missing -= need[c] > 0# s存在一个c就把所需长度missing减去一个 if need[c] > 0: missing -= 1
            if need[c] > 0: missing -= 1# 如果missing == 0 证明当前区域包含所有的字母
            need[c] -= 1#同时也把原Counter减少一个
            if not missing:# not 只有是0，才是True,其他都是False。 在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False 
                while i < j and need[s[i]] < 0:# need[s[i]]<0证明后面出现过很多次s[i]，可以缩短左边，即是增加 i
                    need[s[i]] += 1
                    i += 1
                if not End or j - i <= End - Start:#End和Start保持着最短距离
                    Start, End = i, j
        return s[Start:End]
    
    
    def minWindow1(self, s, t):#这个解释其实不太好理解
        need = collections.Counter(t)            #hash table to store char frequency # need Counter({'A': 1, 'B': 1, 'C': 1})
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):          #index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:                     #match all chars
                while i < j and need[s[i]] < 0:  #remove chars to find the real start, need[s[i]]<0证明后面出现过很多次s[i]，可以缩短，即是增加i
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                missing += 1                     #we missed this first char, so add missing by 1
                if end == 0 or j-i < end-start:  #update window
                    start, end = i, j
                i += 1                           #update i to start+1 for next window
        return s[start:end]
    
if __name__ == "__main__":
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    