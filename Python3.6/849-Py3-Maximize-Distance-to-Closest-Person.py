# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 21:11:22 2018

@author: hjiang
"""
"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """ # result 最小也为1
        prev, result = -1, 1 # 双指针，prev是前面那个， result记录， i是当前的，也可以认为是后面的
        for i in range(len(seats)):
            if seats[i]: # seats[i]不为1,prev不会更新
                if prev < 0:
                    result = i
                else:
                    result = max(result, (i-prev)//2)# 此处表现i是后面的指针，或是当前指针
                prev = i #prev更新
        return max(result, len(seats)-1-prev) #len(seats)-1-prev 是用来修正 1，0，0，0这种序列的
    
if __name__ == "__main__":
#    print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))
    print(Solution().maxDistToClosest([1,0,0,0]))
    
    
    
    
    
    
    
    
    
    