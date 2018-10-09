# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 15:33:33 2018

@author: hjiang
"""

class Solution2(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def binarySearch(A, target, compare):
            start, end = 0, len(A) - 1
            while start <= end:
                mid = start + (end - start) / 2
                if compare(target, A[mid]):
                    end = mid - 1
                else:
                    start = mid + 1
            return start

        class BIT(object):
            def __init__(self, n):
                self.__bit = [0] * n

            def add(self, i, val):
                while i < len(self.__bit):
                    self.__bit[i] += val
                    i += (i & -i)
    
            def query(self, i):
                ret = 0
                while i > 0:
                    ret += self.__bit[i]
                    i -= (i & -i)
                return ret

        # Get the place (position in the ascending order) of each number.
        sorted_nums, places = sorted(nums), [0] * len(nums)
        for i, num in enumerate(nums):
            places[i] = binarySearch(sorted_nums, num, lambda x, y: x <= y)

        # Count the smaller elements after the number.
        ans, bit= [0] * len(nums), BIT(len(nums) + 1)
        for i in reversed(xrange(len(nums))):
#            print(i)
            ans[i] = bit.query(places[i])
            bit.add(places[i] + 1, 1)
        return ans
    
if __name__ == "__main__":
    print (Solution2().countSmaller([5, 2, 6, 3, 7,1,1,1]))
    
    
    
    
    
    