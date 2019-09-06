# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:02:32 2019

@author: hjiang
"""

"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""




# Time:  O(logn) = O(1), n is the value of the integer, which is less than 2^31 - 1
# Space: O(1)    
    
class Solution1:#看这个把，代码比较简单一点
    def numberToWords(self, num):
        if num == 0: return "Zero"
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]#注意不能写成[to19[n-1]],因为n = 0时，返回Nineteen。to19[-1:0]返回的是[]（空）
            if n < 100:
                return [tens[n//10-2]] + words(n%10)
            if n < 1000:
                return [to19[n//100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):#1表示p从1开始数
                if n < 1000**(p+1):
                    return words(n//1000**p) + [w] + words(n%1000**p)#注意，不满足million，自然单位就是thousand
        return ' '.join(words(num))
    
if __name__ == "__main__":
    ans = "Twenty"
    test1 = Solution1().numberToWords(56)
    print(test1)
    print(ans == test1)

## Time:  O(logn) = O(1), n is the value of the integer, which is less than 2^31 - 1
## Space: O(1)
#
#class Solution(object):
#    def numberToWords(self, num):
#        """
#        :type num: int
#        :rtype: str
#        """
#        if num == 0:
#            return "Zero"
#
#        lookup = {0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
#                  10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
#                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", \
#                  20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
#        unit = ["", "Thousand", "Million", "Billion"]
#
#        res, i = [], 0
#        while num:
#            cur = num % 1000
#            if num % 1000:
#                res.append(self.threeDigits(cur, lookup, unit[i]))
#            num //= 1000
#            i += 1
#        return " ".join(res[::-1])#逆序
#
#    def threeDigits(self, num, lookup, unit):
#        res = []
#        if num // 100:
#            res = [lookup[num // 100] + " " + "Hundred"]
#        if num % 100:
#            res.append(self.twoDigits(num % 100, lookup))
#        if unit != "":
#            res.append(unit)
#        return " ".join(res)
#
#    def twoDigits(self, num, lookup):
#        if num in lookup:
#            return lookup[num]
#        return lookup[(num // 10) * 10] + " " + lookup[num % 10]
#    


    
    
    
    
    
    
    
    
    
    