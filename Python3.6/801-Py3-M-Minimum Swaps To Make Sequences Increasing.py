# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:31:52 2019

@author: hjiang
"""

"""
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the 
same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  
(A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  
It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
Note:

A, B are arrays with the same length, and that length will be in the range [1, 1000].
A[i], B[i] are integer values in the range [0, 2000].
https://blog.csdn.net/fuxuemingzhu/article/details/83269027
https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-801-minimum-swaps-to-make-sequences-increasing/
这个是有两种状态，交换和保持，由于不知道i是由i-1怎么搞来的，所以就是需要两个数组，分情况讨论
每次看两位，一共就有四种情况：1/2位，交换/不交换
"""
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        N = len(A)
        keep = [float('inf')] * N#保持第[i]位需要的操作，包括之前的操作
        swap = [float('inf')] * N#交换第[i]位需要的操作，包括之前的操作
        keep[0] = 0
        swap[0] = 1
        for i in range(1, N):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                keep[i] = keep[i - 1]#可以完全不用换
                swap[i] = swap[i - 1] + 1#可以把之前的和当前的都换了
            if A[i] > B[i - 1] and B[i] > A[i - 1]:#
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
        return min(keep[N - 1], swap[N - 1])
    
    
    
    
    
    
    
    
    
    
    
    