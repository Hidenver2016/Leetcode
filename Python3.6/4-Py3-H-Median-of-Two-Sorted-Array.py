# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:17:10 2018

@author: hjiang
"""

#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
#You may assume nums1 and nums2 cannot be both empty.
#
#Example 1:
#
#nums1 = [1, 3]
#nums2 = [2]
#
#The median is 2.0
#Example 2:
#
#nums1 = [1, 2]
#nums2 = [3, 4]
#
#The median is (2 + 3)/2 = 2.5

# Time:  O(log(min(m, n)))
# Space: O(1)
 
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# 看到log就只能能用二分法，本题的关键在于，序列都是排好队的， 只需要用二分法找出 (len1 + len2)//2 和 (len1 + len2)//2 + 1

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1: 
            return self.getKth(nums1, nums2, (len1 + len2)//2 + 1)
        else:
            return (self.getKth(nums1, nums2, (len1 + len2)//2) + self.getKth(nums1, nums2, (len1 + len2)//2 + 1)) * 0.5

    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)

        left, right = 0, m    
        while left < right: # 因为是排好队的，所以left>right,就无需再找
            mid = left + (right - left) // 2
            if 0 <= k - 1 - mid < n and A[mid] >= B[k - 1 - mid]:
                right = mid
            else:
                left = mid + 1

        Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
        Bj = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")
#        Bj = B[k - 1 - mid] if k - 1 - mid >= 0 else float("-inf") 不可以，偶数是错的！！！

        return max(Ai_minus_1, Bj)
    
#https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn))-solution-with-explanation
class Solution1:
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
    
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
    
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])
    
                if (m + n) % 2 == 1:
                    return max_of_left
    
                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])
    
                return (max_of_left + min_of_right) / 2.0
#http://www.voidcn.com/article/p-hqjueegu-mm.html
#https://www.cnblogs.com/zuoyuan/p/3759682.html
"""
首先我们来看如何找到两个数列的第k小个数，即程序中getKth(A, B , k)函数的实现。
用一个例子来说明这个问题：A = {1，3，5，7}；B = {2，4，6，8，9，10}；
如果要求第7个小的数，A数列的元素个数为4，B数列的元素个数为6；k/2 = 7/2 = 3，
而A中的第3个数A[2]=5；B中的第3个数B[2]=6；
而A[2]<B[2]；则A[0]，A[1]，A[2]中必然不可能有第7个小的数。
因为A[2]<B[2]，所以比A[2]小的数最多可能为A[0], A[1], B[0], B[1]这四个数，也就是说A[2]最多可能是第5个大的数，
由于我们要求的是getKth(A, B, 7)；现在就变成了求getKth(A', B, 4)；即A' = {7}；B不变，求这两个数列的第4个小的数，
因为A[0]，A[1]，A[2]中没有解，所以我们直接删掉它们就可以了。这个可以使用递归来实现。
"""
class Solution3(object):#前面的太难了，看这个 (2刷，29/July/2019,还是觉得很难)

    def getKth(self, A, B, k):
        len_a,len_b = len(A),len(B)
        # keep len(A) < len(B)
        if len_a > len_b:
            return self.getKth(B, A, k)
        # when A is empty, return the kth minimal num in B
        if len_a == 0:
            return B[k - 1]#第k个最小的数，k是从1开始的，不是0
        # if k == 1, return the minimal num between A[0] and B[0]
        if k == 1:#第k个最小的数，k是从1开始的
            return min(A[0],B[0])
        pa = min(k // 2,len_a)
        # we have make len(B) > len(A), so pb always less than or equal to len(B) 
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:],B,k - pa)#如果上面的条件满足，那么意味着A[0]到A[pa-1]都是没用的，直接删掉就可以了
        else:
            return self.getKth(A,B[pb:],k - pb)

    def findMedianSortedArrays(self, nums1, nums2):
        """ :type nums1: List[int] :type nums2: List[int] :rtype: float """
        if not nums1 and not nums2:
            return None
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.getKth(nums1, nums2, n // 2 + 1)#奇数就是中间的数
        else:
            return (self.getKth(nums1, nums2, n // 2) + self.getKth(nums1, nums2, n // 2 + 1) ) * 0.5#偶数就是两个数的均值
        
#https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms        
class Solution4:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   
        
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]
        
        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

if __name__ == "__main__":
    print (Solution1().findMedianSortedArrays([1, 3, 5, 7,9,11], [2, 4, 6,8,10,12]))
    print (Solution1().findMedianSortedArrays([1, 3, 7,8,9], [20, 40, 80]))
    

















    
    
    
    
    
    
    
    
    
