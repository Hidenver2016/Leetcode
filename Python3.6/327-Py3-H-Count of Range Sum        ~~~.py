# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:19:24 2019

@author: hjiang
"""

"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
"""

#https://leetcode.com/problems/count-of-range-sum/discuss/77991/Short-and-simple-O(n-log-n)
#https://www.hrwhisper.me/leetcode-count-of-range-sum/
#Time: O(n log n)
"""
因为是要计算区间, 因此我们可以将其前n个元素求和放到一个数组中, 这样当我们我计算区间[i, j]的和时, 只要用sum[j+1] - sum[i]即可, 
这样就可以在O(1)的时间取得任意区间的和. 
"""
class FenwickTree(object):
    def __init__(self, n):
        self.sum_array = [0] * (n + 1)
        self.n = n
 
    def lowbit(self, x):
        return x & -x
 
    def add(self, x, val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)
 
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res
  
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums: return 0
        sum_array = [upper, lower - 1]
        total = 0
        for num in nums:
            total += num
            sum_array += [total, total + lower - 1, total + upper]
 
        index = {}
        for i, x in enumerate(sorted(set(sum_array))):
            index[x] = i + 1
 
        tree = FenwickTree(len(index))
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            tree.add(index[total], 1)
            total -= nums[i]
            ans += tree.sum(index[upper + total]) - tree.sum(index[lower + total - 1])
        return ans
    
#https://leetcode.com/problems/count-of-range-sum/discuss/77986/O(NlogN)-Python-solution-binary-indexed-tree-268-ms
"""
Sum[k] is the sum of first k numbers. O(N^2) solution is

for j in range(n + 1):
    for i in range(j):
        if lower <= Sum[j] - Sum[i] <= upper: res += 1
This is equal to:

collection = empty
for sum_j in Sum:
    sum_i_count = how many sum_i in this collection that sum_j - upper <= sum_i <= sum_j - lower
    res += sum_i_count
    put sum_j into this collection
    
With Binary indexed tree, counting sum_i number is O(logN), putting sum_i into tree is also O(logN). 
Here we store the index of sortSum in the tree. Since index of BITree starts from 1, 
we need bisect.bisect_left(sortSum, sum_j) + 1 for update().
"""
class Solution0:
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        Sum, BITree = [0] * (n + 1), [0] * (n + 2)
        
        def count(x):
            s = 0
            while x:
                s += BITree[x]
                x -= (x & -x)
            return s
        
        def update(x):
            while x <= n + 1:
                BITree[x] += 1
                x += (x & -x)
                
        for i in range(n):
            Sum[i + 1] = Sum[i] + nums[i]
        sortSum, res = sorted(Sum), 0
        for sum_j in Sum:
            sum_i_count = count(bisect.bisect_right(sortSum, sum_j - lower)) - count(bisect.bisect_left(sortSum, sum_j - upper))
            res += sum_i_count
            update(bisect.bisect_left(sortSum, sum_j) + 1)
        return res
#https://leetcode.com/problems/count-of-range-sum/discuss/77991/Short-and-simple-O(n-log-n)
#https://blog.csdn.net/qq508618087/article/details/51435944
"""
First compute the prefix sums: first[m] is the sum of the first m numbers.
Then the sum of any subarray nums[i:k] is simply first[k] - first[i].
So we just need to count those where first[k] - first[i] is in [lower,upper].

To find those pairs, I use mergesort with embedded counting. 
The pairs in the left half and the pairs in the right half get counted in the recursive calls. 
We just need to also count the pairs that use both halves.

For each left in first[lo:mid] I find all right in first[mid:hi] so that 
right - left lies in [lower, upper]. Because the halves are sorted, 
these fitting right values are a subarray first[i:j]. With increasing left we must also increase right, 
meaning must we leave out first[i] if it's too small and and we must include first[j] if it's small enough.

Besides the counting, I also need to actually merge the halves for the sorting. 
I let sorted do that, which uses Timsort and takes linear time to recognize and merge the already sorted halves.
在合并左右数组的时候对于左边数组中的每一个元素在右边数组找到一个范围, 使得在这个范围中的的元素与左边的元素构成的区间和落在[lower, upper]之间.  
即在右边数组找到两个边界, 设为m, n, 其中m是在右边数组中第一个使得sum[m] - sum[i] >= lower的位置, n是第一个使得sum[n] - sum[i] > upper的位置, 
这样n-m就是与左边元素i所构成的位于[lower, upper]范围的区间个数. 因为左右两边都是已经有序的, 这样可以避免不必要的比较.
--------------------- 
作者：小榕流光 
来源：CSDN 
原文：https://blog.csdn.net/qq508618087/article/details/51435944 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
def countRangeSum1(self, nums, lower, upper):# 看这个把，重点掌握归并排序好了%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    first = [0]
    for num in nums:
        first.append(first[-1] + num)
    def sort(lo, hi):
        mid = (lo + hi) // 2
        if mid == lo:
            return 0
        count = sort(lo, mid) + sort(mid, hi)
        i = j = mid
        for left in first[lo:mid]:
            while i < hi and first[i] - left <  lower: i += 1
            while j < hi and first[j] - left <= upper: j += 1
            count += j - i
        first[lo:hi] = sorted(first[lo:hi])
        return count
    return sort(0, len(first)) 
"""
# Recursively implementation of Merge Sort
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(L):
    if len(L) <= 1:
        # When D&C to 1 element, just return it
        return L
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    # conquer sub-problem recursively
    return merge(left, right)
    # return the answer of sub-problem


if __name__ == "__main__":
    test = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print("original:", test)
    print("Sorted:", merge_sort(test)) 
"""
#https://leetcode.com/problems/count-of-range-sum/discuss/78016/Very-concise-solution-in-Python-with-explanation
# Time: O(n^2) 
"""
Accumulate sum of elements in array order. Check if any existing sum before which satisfy:
lower <= thisSum - prevSum <= upper, which also becomes:
thisSum - upper <= prevSum <= thisSum - lower
The total number of prefix which satisfy above condition is the answer
此题太难，上面描述很准确，但是不好理解
"""
import bisect
class Solution1(object):#可能是因为bisect提前compile了才非常快
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix,thisSum,ans = [0],0,0
        for n in nums:
            thisSum += n
            ans += bisect.bisect_right(prefix, thisSum-lower) - bisect.bisect_left(prefix, thisSum-upper)
            bisect.insort(prefix, thisSum)#O(n)
        return ans
    
if __name__ == "__main__":
    print(Solution1().countRangeSum([-2,5,-1],-2,2))
#    print(Solution0().countRangeSum([-2,5,-1],-2,2))
    
    

    
    
    
    
    
    
    
    
    
    
    