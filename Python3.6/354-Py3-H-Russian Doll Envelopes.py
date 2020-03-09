# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:08:13 2019

@author: hjiang
"""

"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). 
One envelope can fit into another if and only if both the width and height of one envelope 
is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
https://leetcode.com/problems/russian-doll-envelopes/discuss/82761/Python-O(nlogn)-O(n)-solution-beats-97-with-explanation
https://www.cnblogs.com/grandyang/p/5568818.html
我们首先要做的还是给信封排序，但是这次排序和上面有些不同，信封的宽度还是从小到大排，但是宽度相等时，我们让高度大的在前面。
[[2, 3], [5, 4], [6, 7], [6, 5], [6, 4]]
那么现在问题就简化了成了找高度数字中的LIS，完全就和之前那道300 Longest Increasing Subsequence一样了，所以我们还是使用之前那题解法来做
"""

class Solution(object):
    def maxEnvelopes(self, envelopes):#看这个，自己写的
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))#because when the width is the same, the envelope with greater height comes first.

        tails = [0] * len(envelopes)# 300 题
        size = 0
        for i, e in enumerate(envelopes):
            l, r = 0, size
            while l < r:
                m = (l + r) // 2
                if tails[m] >= e[1]:
                    r = m
                else:
                    l = m + 1
            tails[l] = e[1]
            size = max(l+1, size)
        return size


import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):#这个就是把上面的二分法简化成了自己有的模块
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))#because when the width is the same, the envelope with greater height comes first.
        h=[]
        for i, e in enumerate(envelopes,0):#start from 0, 省掉也一样
            j=bisect.bisect_left(h,e[1])
            if j<len(h):
                h[j]=e[1]
            else:
                h.append(e[1])
        return len(h)
        # tails = [0] * len(envelopes)
        # size = 0
        # for i, e in enumerate(envelopes):
        #     l, r = 0, size
        #     while l < r:
        #         m = (l + r) // 2
        #         if tails[m] >= e[1]:
        #             r = m
        #         else:
        #             l = m + 1
        #     tails[l] = e[1]
        #     size = max(l+1, size)
        # return size
    
if __name__ == "__main__":
    Input = [[5,4],[6,4],[6,7],[2,3], [6,5]]
    print(Solution().maxEnvelopes(Input))
    
# # 300题，    Longest Increasing Subsequence
# class Solution1:
#     def lengthOfLIS(self, nums):#看这个
#         tails = [0] * len(nums)
#         size = 0
#         for x in nums:
#             l, r = 0, size
#             while l < r:#从左边插入的好处就是，一旦有比较小的数字就会把右侧大的数字原味置代替，除非有新的更大的数字进来，否则tail这个数组的大小是不会增加的
#                 m = (l + r) // 2
#                 if tails[m] >= x:
#                     r = m
#                 else:
#                     l = m + 1
#             tails[l] = x #这个size实际上是tail的size,那么上面那个二分法实际上也是在找x在tails中的位置（有重复数字，就从左边插入）
#             size = max(l + 1, size)
#         return size
    
    
    
    
    
    
    