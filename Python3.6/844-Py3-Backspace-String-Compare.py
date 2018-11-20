# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:36:19 2018

@author: hjiang
"""
"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
Time： O(2N)
Space: O(2)
"""



class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s1 = []
        t1 = []
        
        for i in S:
            if i == "#" and s1: #注意，有子序列才可以弹出
                s1.pop()
            elif i != "#":
                s1.append(i)
                
        for j in T:
            if j == "#" and t1:
                t1.pop()
            elif j != "#":
                t1.append(j)
                   
        return s1 == t1
            
if __name__ == "__main__":
    print(Solution().backspaceCompare("ab#c","ad#c")) # True
    print(Solution().backspaceCompare("ab##","c#d#")) # True
    print(Solution().backspaceCompare("a##c","#a#c")) # True
          
    
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          