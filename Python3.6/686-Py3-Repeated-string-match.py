# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:49:22 2018

@author: hjiang
"""

"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. 
If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; 
and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
关键： ceil是-(-len(B) // len(A))此题的关键，如果不用的话，“len(B)//len(A)+3”才会比较保险

"""

#class Solution:
#    def repeatedStringMatch(self, A, B):
#        """
#        :type A: str
#        :type B: str
#        :rtype: int
#        """
#        for i in range(1,len(B)//len(A)+1):
#            C = i*A
#            if (len(C)>=len(B)):
#                for j in range(len(C)-len(B)+1):
#                    if C[j:j+len(B)] == B:
#                        return i
#        return -1
    
class Solution1(object):
    def repeatedStringMatch(self, A, B):
        times = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a)) 注意要取ceil
        for i in range(2):
          if B in (A * (times + i)):
            return times + i
        return -1
    
class Solution2:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        for i in range(1,len(B)//len(A)+3):
            C = i*A
            if (len(C)>=len(B)) and B in C:
                return i
        return -1

if __name__ == "__main__":
#    print(Solution2().repeatedStringMatch("a", "aa"))
#    print(Solution2().repeatedStringMatch("abcd", "cdabcdab"))
    print(Solution1().repeatedStringMatch("abc", "cabcabca"))
    