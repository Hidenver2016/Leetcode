# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:54:00 2018

@author: hjiang
"""

"""
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. 
The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, 
determine if the frog is able to cross the river by landing on the last stone. 
Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. 
Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
"""
# Time:  O(n) ~ O(n^2)
# Space: O(n)
class Solution(object):
    def canCross(self, stones):
        self.memo = set()
        target = stones[-1]
        stones = set(stones)

        res = self.dfs(stones, 1, 1, target)
        return res

    def dfs(self, stones, cur, speed, target):
#        print(cur, speed, self.memo)
        # check memo
        if (cur, speed) in self.memo:
            return False

        if cur==target:
            return True
        
        if cur>target or cur<0 or speed<=0 or cur not in stones:
            return False
        # dfs
        candidate = [speed-1, speed, speed+1]
        for c in candidate:
            if (cur + c) in stones:
                if self.dfs(stones, cur+c, c, target):# 关键！ c用作speed的输入
                    return True

        self.memo.add((cur,speed))
        return False
    
if __name__ == "__main__":
    print(Solution().canCross([0,1,3,5,6,8,12,17]))
    print(Solution().canCross([0,1,2,3,4,8,9,11]))
    
    
# Time:  O(n) ~ O(n^2)
# Space: O(n)

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False

        last_jump_units = {s: set() for s in stones}
        last_jump_units[1].add(1)
        for s in stones[:-1]:
            for j in last_jump_units[s]:
                for k in (j-1, j, j+1):
                    if k > 0 and s+k in last_jump_units:
                        last_jump_units[s+k].add(k)
        return bool(last_jump_units[stones[-1]])
    























