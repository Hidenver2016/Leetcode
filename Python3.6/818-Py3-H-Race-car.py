# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:19:31 2018

@author: hjiang
"""

"""
Your car starts at position 0 and speed +1 on an infinite number line.  
(Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A 
(accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: 
if your speed is positive then speed = -1 , otherwise speed = 1.  
(Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, 
and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.
 

Note:
https://www.jianshu.com/p/bad491f550fa
https://blog.csdn.net/magicbean2/article/details/80333734
花花15分13秒开始，第一个视频
1 <= target <= 10000.

关键: 三种情况： 1.正好的， 2冲过去回来的，3冲过去回来再回去的
"""
# Time : O(nlogn), n is the value of the target, 子问题需要的时间是k,k就是logn（主要是指第三个问题）, 然后外面的循环是n,所以是nlogn
# Space: O(n) 空间复杂度是target (dp就是O(n), 加上递归深度logn,所以是n+logn
class Solution(object):
    def racecar(self, target):
        dp = [0] * (target+1)
        for i in range(1, target+1):
            # 2^(k-1) <= i < 2^k
            k = i.bit_length()

            # case 1. drive exactly i at best
            #         seq(i) = A^k
            if i == 2**k-1:#这里注意看都是按照边界条件来的， 例如target = 1, 则k = 1， dp[1] = 1,这个就是正确的结果
                dp[i] = k
                continue

            # case 2. drive cross i at 2^k-1, and turn back to i
            #         seq(i) = A^k -> R -> seq(2^k-1 - i)
            dp[i] = k+1 + dp[2**k-1 - i] #冲过去，掉头一次的情况，所以有一个+1，然后是反向加速，要走的距离就是走多了的(2**k-1 - i) 

            # case 3. drive less then 2^k-1, and turn back some distance, 不冲过去，在前面停下来，搞两次调头
            #         and turn back again to make the direction is the same
            #         seq(i) = shortest(seq(i), A^(k-1) -> R -> A^j -> R ->
            #                                   seq(i - (2^(k-1)-1) + (2^j-1)),
            #                  where 0 <= j < k-1)
            #         => dp[i] = min(dp[i], (k-1) + 1 + j + 1 +
            #                               dp[i - (2**(k-1)-1) + (2**j-1)])
            for j in range(k-1): #对应于花花的讲义，此处j是讲义里面的m, k是n, i是t，
                dp[i] = min(dp[i], k+j+1 + dp[i - 2**(k-1) + 2**j])# 先走k-1步，掉头，再走j步，再掉头

        return dp[-1]
    
    
if __name__ == "__main__":
    print(Solution().racecar(10000))    
    
    
    
    
    
    
    
    
    