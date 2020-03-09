# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:54:54 2019

@author: hjiang
"""

"""
Given a non-empty 2D matrix matrix and an integer k, 
find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
http://bookshadow.com/weblog/2016/06/22/leetcode-max-sum-of-sub-matrix-no-larger-than-k/
https://www.hrwhisper.me/leetcode-max-sum-rectangle-no-larger-k/
https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98


思路：

朴素的思想为，枚举起始行，枚举结束行，枚举起始列，枚举终止列。。。。。O(m^2 * n^2)

这里用到一个技巧就是，进行求和时，我们可以把二维的合并成一维，然后就变为求一维的解。

比如对于矩阵：

[1, 0, 1],
[0, -2, 3]

进行起始行为0，终止行为1时，可以进行列的求和，即[1, -2, 4]中不超过k的最大值。

求和的问题解决完，还有一个是不超过k. 这里我参考了 https://leetcode.com/discuss/109705/java-binary-search-solution-time-complexity-min-max-log-max 的方法

使用了二分搜索。对于当前的和为sum，我们只需要找到一个最小的数x，使得 sum – k <=x，这样可以保证sum – x <=k。

这里需要注意，当行远大于列的时候怎么办呢？转换成列的枚举 即可。

在代码实现上，我们只需要让 m 永远小于 n即可。这样复杂度总是为O(m^2*n*log n)

这个题太难，还是用暴力解法算了，考虑Kadane_algorithm file, 臣妾做不到，只能理解这么多了（现在可以理解了）
这里有解释https://zhuanlan.zhihu.com/p/96014673
"""
# Time:  O(min(m, n)^2 * max(m, n) * log(max(m, n)))
# Space: O(max(m, n))

from bisect import bisect_left, insort_right

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):# 看这个，这个Kadane算法是用来找最小的x 
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0

        m = min(len(matrix), len(matrix[0]))
        n = max(len(matrix), len(matrix[0]))
        result = float("-inf")

        for i in range(m): #这个是针对行，进行列的求和，（列数大于行数的情况下） 两个m的循环，证明考虑了m中的子方块
            sums = [0] * n
            for j in range(i, m):# 往下走
                for l in range(n):# 往右走
                    sums[l] += matrix[j][l] if m == len(matrix) else matrix[l][j]

                # Find the max subarray no more than K. 返回最接近K的值 这个地方有问题
                accu_sum_set, accu_sum = [0], 0
                for sum in sums:
                    accu_sum += sum
                    it = bisect_left(accu_sum_set, accu_sum - k)  # Time: O(logn) 放置于左边，求左边的index, accu_sum - k 就是 sum-k， 寻找x的位置
                    if it != len(accu_sum_set):#如果相等，证明accu_sum太大了，result不更新
                        result = max(result, accu_sum - accu_sum_set[it]) # accu_sum_set[it]就是序列中最接近sum-k的数，这里有个减号，就是想让x最小，accu_sum - accu_sum_set[it]最接近k
                    insort_right(accu_sum_set, accu_sum)  # Time: O(n) 放置于右边， 上面一行就是sum-x,是能力范围之内的，最接近的sum-x, 就是要的result

        return result
    
    
"""
Created on Mon Jan  7 23:01:43 2019

@author: hjiang
"""

"""
https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98
Kadane algorithm
查找一个序列中最接近(小于等于)k的子序列的和
使用了二分搜索。对于当前的和为sum，我们只需要找到一个最小的数x，使得 sum – k <=x，这样可以保证sum – x <=k。
"""
#from bisect import bisect_left, insort_right
#result = float("-inf")
#k = 7
#sums = [-2,1,-3,4,-1,2,1,-5,4]
#accu_sum_set, accu_sum = [0], 0
#for sum in sums:
#    accu_sum += sum
#    it = bisect_left(accu_sum_set, accu_sum - k)  # Time: O(logn)， accu_sum - k 就是 sum-k
#    if it != len(accu_sum_set):
#        print (sum)
#        print ("accu_sum, accu_sum_set[it], accu_sum - accu_sum_set[it]:",accu_sum, accu_sum_set[it],accu_sum - accu_sum_set[it])
#        result = max(result, accu_sum - accu_sum_set[it])# accu_sum_set[it]就是序列中最接近sum-k的数，这里有个减号，就是想让x最小
#    insort_right(accu_sum_set, accu_sum)  # Time: O(n)
#    
#print(result)   


class Solution1:
    def maxSumSubmatrix(self, matrix, k):#先记住这个好了,这个会超时
        if not matrix or not matrix[0]: return 0
        m = len(matrix[0]); n = len(matrix); res = -float("inf")
        sum1 = [[0 for _ in range(m)] for _ in range(n)]
        t = 0; d = 0
        for i in range(n):
            for j in range(m):
                t = matrix[i][j]
                if i > 0: t += sum1[i - 1][j]
                if j > 0: t += sum1[i][j - 1]
                if i > 0 and j > 0: t -= sum1[i - 1][j - 1]#注意这里是减号
                sum1[i][j] = t
                for r in range(i + 1):
                    for l in range(j + 1):
                        d = sum1[i][j]
                        if r > 0: d -= sum1[r - 1][j]
                        if l > 0: d -= sum1[i][l - 1]
                        if r > 0 and l > 0: d += sum1[r - 1][l - 1]#注意这里是加号
                        if d <= k: res = max(res, d)
        return res

if __name__ == "__main__":
    matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]; k = 3

    print(Solution().maxSumSubmatrix(matrix, k))
                        
                            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    