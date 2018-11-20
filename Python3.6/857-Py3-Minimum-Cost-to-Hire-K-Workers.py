# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:35:53 2018

@author: hjiang
"""

"""
There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, 
we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 

Note:

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.

https://blog.csdn.net/fuxuemingzhu/article/details/82942731
https://buptwc.github.io/2018/06/26/Leetcode-857-Minimum-Cost-to-Hire-K-Workers/
Time: O(nlogn)
Space: O(n)
即需要按照K个工人中的最高期望价性比给这K个人开工资
使用了一个大根堆，来获取K个工人的最大的价性比，作为K个工人的价性比，使用qsum保存K个工人的质量和。要给他们付的工资就是qsum * 最大性价比。
heapq都是默认最小堆
"""
import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        works = sorted([(w / float(q), q) for w, q in zip(wage, quality)]) #价性比来做排序
        que = []
        qsum = 0
        res = float("inf")
        for rate, q in works:
            heapq.heappush(que, -q) # 此处加负号是因为heapq是默认最小堆
            qsum += q
            if len(que) > K:
                qsum += heapq.heappop(que) # 把quality最大的弹出掉
            if len(que) == K:
                res = min(res, qsum * rate)
        return res
    
if __name__ == "__main__":
#    print(Solution().mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))
    print(Solution().mincostToHireWorkers([10,20,5], [70,50,30], 2))
    
    
    
    
    
    
    
    
    