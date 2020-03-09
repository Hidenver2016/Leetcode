# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 00:48:46 2020

@author: hjiang
"""

"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:



Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Note:

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000

这个题要看图leetcode的原图

这个题目还考智力

1. 先给两个list count
2. 计数，找出同样位置为同样数字的有多少，分开计数
3. 满足要求的为countA[i] + countB[i] - same[i] == len(A)
4. 找出最小的即可min(countA[i], countB[i]) - same[i]
"""


from collections import Counter

class Solution:
    def minDominoRotations(self, A, B):
        if len(A) != len(B): return -1
        same, countA, countB = Counter(), Counter(A), Counter(B)
        for a, b in zip(A, B):
            if a == b:
                same[a] += 1
        for i in range(1, 7):
            if countA[i] + countB[i] - same[i] == len(A):
                return min(countA[i], countB[i]) - same[i]        
        return -1
    
    
    
    
    
    
    
    