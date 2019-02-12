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
http://www.cnblogs.com/grandyang/p/5078490.html
这个题目也可以用二分法，见上
那么我们为了提高运算效率，首先可以使用用二分搜索法，思路是将给定数组从最后一个开始，
用二分法插入到一个新的数组，这样新数组就是有序的，那么此时该数字在新数组中的坐标就是原数组中其右边所有较小数字的个数
"""

class Solution00:#这个题目二分法也可以做
    def countSmaller(self, nums):
        n = len(nums)
        if n == 0: return []
        res = [None] * n
        t = []
        for i in reversed(range(n)):
            l, r = 0, len(t)
            while l < r:
                mid = l + (r - l) // 2
                if t[mid] >= nums[i]:#原数组在新数组中的位置
                    r = mid
                else:
                    l = mid + 1
            res[i] = r #坐标是在这里被记录的，所以原数组从右向左向新数组插入值就是在比较右边有多少个数比他小，如果是最后记录就迟了
            t.insert(r, nums[i])#注意，这个地方t.insert(t.begin() + right, nums[i]);
        return res

# Time:  O(nlogn)
# Space: O(n)

class Solution0(object):#git的答案归并排序
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def countAndMergeSort(num_idxs, start, end, counts):
            if end - start <= 0:  # The size of range [start, end] less than 2 is always with count 0.
                return 0

            mid = start + (end - start) / 2
            countAndMergeSort(num_idxs, start, mid, counts)
            countAndMergeSort(num_idxs, mid + 1, end, counts)
            r = mid + 1
            tmp = []
            for i in range(start, mid + 1):
                # Merge the two sorted arrays into tmp.
                while r <= end and num_idxs[r][0] < num_idxs[i][0]:
                    tmp.append(num_idxs[r])
                    r += 1
                tmp.append(num_idxs[i])
                counts[num_idxs[i][1]] += r - (mid + 1)

            # Copy tmp back to num_idxs
            num_idxs[start:start+len(tmp)] = tmp

        num_idxs = []
        counts = [0] * len(nums)
        for i, num in enumerate(nums):
            num_idxs.append((num, i))
        countAndMergeSort(num_idxs, 0, len(num_idxs) - 1, counts)
        return counts

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
    print (Solution00().countSmaller([5, 2, 6, 1]))
#    print (Solution2().countSmaller([6, 5, 4,3, 2, 1]))



#s = [3, 4, 1, 7, 2]
#
#sorted(range(len(s)), key=lambda k: s[k])
#Out[4]: [2, 4, 0, 1, 3]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    