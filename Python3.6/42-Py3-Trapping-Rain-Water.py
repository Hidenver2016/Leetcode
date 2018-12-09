# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:18:59 2018

@author: hjiang
"""

#Given n non-negative integers representing an elevation map where the width of each bar is 1, 
#compute how much water it is able to trap after raining.
#
#
#The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
#In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
#Example:
#
#Input: [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6

A = [0,1,0,2,1,0,1,3,2,1,2,1]
result = 0
top = 0
for i in range(len(A)):
    if A[top] < A[i]:
        top = i

second_top = 0
for i in range(top):
    print ("A[second_top], A[i]", A[second_top], A[i])
    if A[second_top] < A[i]:
        second_top = i
    result += A[second_top] - A[i]
    
second_top = len(A) - 1
for i in reversed(range(top, len(A))):
    print ("A[second_top], A[i]", A[second_top], A[i])
    if A[second_top] < A[i]:
        second_top = i
    result += A[second_top] - A[i]

print (result)


# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        top = 0
        for i in range(len(A)):
            if A[top] < A[i]:
                top = i

        second_top = 0
        for i in range(top):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]

        second_top = len(A) - 1
        for i in reversed(range(top, len(A))):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]

        return result