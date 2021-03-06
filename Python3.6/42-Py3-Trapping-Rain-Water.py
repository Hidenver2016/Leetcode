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

#A = [0,1,0,2,1,0,1,3,2,1,2,1]
#result = 0
#top = 0
#for i in range(len(A)):
#    if A[top] < A[i]:
#        top = i
#
#second_top = 0
#for i in range(top):
#    print ("A[second_top], A[i]", A[second_top], A[i])
#    if A[second_top] < A[i]:
#        second_top = i
#    result += A[second_top] - A[i]
#    
#second_top = len(A) - 1
#for i in reversed(range(top, len(A))):
#    print ("A[second_top], A[i]", A[second_top], A[i])
#    if A[second_top] < A[i]:
#        second_top = i
#    result += A[second_top] - A[i]
#
#print (result)

"""
# Time:  O(n)
# Space: O(1)
#关键是思路：先找最大值，然后从左边开始向最大值过一遍；然后从最右向最大值过一遍。
#原理：里面的水（从左向右或从右向左）会被外面高的挡住 result += A[second_top] - A[i]
"""


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

        second_top = len(A) - 1#第二遍就是查漏补缺，关于边界
        for i in reversed(range(top, len(A))):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]

        return result
"""
最后我们来看一种只需要遍历一次即可的解法，这个算法需要left和right两个指针分别指向数组的首尾位置，
从两边向中间扫描，在当前两指针确定的范围内，先比较两头找出较小值，如果较小值是left指向的值，
则从左向右扫描，如果较小值是right指向的值，则从右向左扫描，若遇到的值比当较小值小，
则将差值存入结果，如遇到的值大，则重新确定新的窗口范围，以此类推直至left和right指针重合，
http://www.cnblogs.com/grandyang/p/4402392.html
"""    
    
class Solution1:#这个方法和11题非常类似，可以一起看
    def trap(self, A):
        l, r =0, len(A)-1
        level, res = 0, 0
        while l < r:
            if A[l] < A[r]:                
                lower = A[l]
                l += 1
            else:                
                lower = A[r]
                r -= 1
#            lower = A[l + 1 if A[l] < A[r] else r - 1]
            level = max(level, lower)
            res += level - lower
        return res
    
if __name__ == "__main__":
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    
    
    
    
    
    
    
    
    
    
    
    
    