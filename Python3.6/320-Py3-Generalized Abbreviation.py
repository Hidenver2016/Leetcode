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

#class Solution(object):
#    def generateAbbreviations(self, word):
#        def helper(word, i, seq, res):
#            if i == len(word): res.append(seq); return
#            for j in range(i, len(word)):
#                num = str(j - i) if j - i > 0 else ''
#                helper(word, j + 1, seq + num + word[j], res)
#            helper(word, len(word), seq + str(len(word) - i), res)
#        res = []
#        helper(word, 0, '', res)
#        return res
    
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, cur, count, res):# pos是现在的positiion, cur是当前序列，count是最后的1，2，3，4数字，res是结果
            if len(word) == pos:
                # Once we reach the end, append current to the res
                res.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                helper(word, pos + 1, cur, count + 1, res) #数字增加
                # Include current position, and zero-out count
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, res)#还有字母补充

        res = []
        helper(word, 0, '', 0, res)
        return res    
    
if __name__ == "__main__":
    print(Solution().generateAbbreviations("word"))