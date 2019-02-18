# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:47:53 2019

@author: hjiang
"""

"""
Given a string, we can "shift" each of its letter to its successive letter, 
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, 
group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
http://www.cnblogs.com/grandyang/p/5204770.html
https://leetcode.com/problems/group-shifted-strings/discuss/67466/1-4-lines-Ruby-and-Python
而其实我们可以更加巧妙的利用偏移字符串的特点，那就是字符串的每个字母和首字符的相对距离都是相等的，
比如abc和efg互为偏移，对于abc来说，b和a的距离是1，c和a的距离是2，对于efg来说，f和e的距离是1，g和e的距离是2。
再来看一个例子，az和yx，z和a的距离是25，x和y的距离也是25(直接相减是-1，这就是要加26然后取余的原因)，
那么这样的话，所有互为偏移的字符串都有个unique的距离差，我们根据这个来建立映射就可以很好的进行单词分组了，这个思路真实太赞了，
参见代码如下：
代码和49题高度类似
"""
#Time:O(n) 估计还要乘一个在每一个单词中循环的次数
#Space:O(n)
import collections
#def groupStrings0(self, strings):
#    groups = collections.defaultdict(list)
#    for s in strings:
#        groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
#    return groups.values()
class Solution:
    def groupStrings(self, strings):
        groups = collections.defaultdict(list)
        for s in strings:
            print(s)
            key_num = tuple((ord(c) + 26 - ord(s[0])) % 26 for c in s)
            groups[key_num].append(s) #用这个比较稳
#            groups[key_num] += s,#一定要注意这个逗号，如果没加就会把s拆散成字母['a', 'b', 'c', 'b', 'c', 'd', 'x', 'y', 'z'],
        return groups.values()
    
if __name__ == "__main__":
    print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))