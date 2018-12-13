# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 15:33:33 2018

@author: hjiang
315-count-of-smaller-numbers-after-self

# Given nums = [5, 2, 6, 1]
#
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].

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
                mid = int(start + (end - start) / 2)
                if compare(target, A[mid]): # compare is <=
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
                    print("update self._BIT__bit[%d]", i)
                    i += (i & -i)
    
            def query(self, i):
                ret = 0
                while i > 0:
                    ret += self.__bit[i]
                    print("sum self._BIT__bit[%d]", i)
                    i -= (i & -i)
                return ret

        # Get the place (position in the ascending order) of each number.
        sorted_nums, places = sorted(nums), [0] * len(nums)
        for i, num in enumerate(nums):
            places[i] = binarySearch(sorted_nums, num, lambda x, y: x <= y)

        # Count the smaller elements after the number.
        ans, bit= [0] * len(nums), BIT(len(nums) + 1)
        for i in reversed(range(len(nums))):
#            print("\n", "This is round %d", i)
            ans[i] = bit.query(places[i])
#            print ("ans is", ans)
            bit.add(places[i] + 1, 1)
#            print("The new bit._BIT__bit is", bit._BIT__bit)
        return ans
    
if __name__ == "__main__":
#    print (Solution2().countSmaller([5, 2, 6, 1]))
    print (Solution2().countSmaller([6, 5, 4,3, 2, 1]))



#s = [3, 4, 1, 7, 2]
#
#sorted(range(len(s)), key=lambda k: s[k])
#Out[4]: [2, 4, 0, 1, 3]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    