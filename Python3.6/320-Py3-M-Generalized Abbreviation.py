# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:42:59 2019

@author: hjiang
"""

"""
Write a function to generate the generalized abbreviations of a word. 

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""

# Time:  O(n * 2^n)
# Space: O(n)

#class Solution0(object):
#    def generateAbbreviations(self, word):
#        def helper(word, index, path, res):
#            if index == len(word): res.append(path); return
#            for i in range(index, len(word)):
#                num = str(i - index) if i - index > 0 else ''
#                helper(word, i + 1, path + num + word[i], res)
#            helper(word, len(word), path + str(len(word) - index), res)
#        res = []
#        helper(word, 0, '', res)
#        return res

class Solution:
    def generateAbbreviations(self, word):
        ans = []
        self.helper(word, 0, '', ans)
        return ans
    def helper(self, word, index, path, ans):
        if len(word) == index:
            ans.append(path)
            return
        for i in range(index, len(word)):
            num = str(i - index) if i - index > 0 else ''
            self.helper(word, i+1, path + num + word[i], ans)#对应于最后是字母的情况
        self.helper(word, len(word), path + str(len(word) - index), ans)#这一行是最后由数字的情况的,还剩下多少，全部变成数字
    
    
#class Solution1(object):
#    def generateAbbreviations(self, word):
#        """
#        :type word: str
#        :rtype: List[str]
#        """
#        def helper(word, pos, cur, count, res):# pos是现在的positiion, cur是当前序列，count是最后的1，2，3，4数字，res是结果
#            if len(word) == pos:
#                # Once we reach the end, append current to the res
#                res.append(cur + str(count) if count > 0 else cur)
#            else:
#                # Skip current position, and increment count
#                helper(word, pos + 1, cur, count + 1, res) #数字增加
#                # Include current position, and zero-out count
#                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, res)#还有字母补充
#
#        res = []
#        helper(word, 0, '', 0, res)
#        return res    
    
if __name__ == "__main__":
    print(Solution().generateAbbreviations("word"))
    
    
    
    
    
    
    
    
    