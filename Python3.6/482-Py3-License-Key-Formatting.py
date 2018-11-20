# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:42:19 2018

@author: hjiang


You are given a license key represented as a string S which consists only alphanumeric character and dashes. 
The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, 
except for the first group which could be shorter than K, but still must contain at least one character. 
Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters 
except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.


"""

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        result = ''
        for i in reversed(range(len(S))):
            if S[i] == '-':
                continue
            if len(result) % (K + 1) == K:
                result += '-'
            result += S[i].upper()
        return "".join(reversed(result))

class Solution1(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        temp = "".join(S.split("-"))
        if len(temp)<K:
            return temp.upper()
        else:
            res = len(temp) % K
            if res!=0:
                part1 = temp[0:res]
                part2 = temp[res:]
                result = part1 + "-" + "-".join(part2[i:i+K] for i in range(0, len(part2), K))
            else:
                result = "-".join(temp[i:i+K] for i in range(0, len(temp), K))
            
            return result.upper() 
                
            
        
    
if __name__ == "__main__":
    print(Solution1().licenseKeyFormatting("2-4A0r7fewf", 4))
    
    

