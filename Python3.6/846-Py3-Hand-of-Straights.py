# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:29:39 2018

@author: hjiang
"""

"""
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, 
and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
 

Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
https://www.bilibili.com/video/av24391209/?p=3
https://leetcode.com/problems/hand-of-straights/discuss/135600/short-and-clear-Python-solution-%2B-B
"""
class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        hand.sort() #先排序
        while hand:
            try:
                base = hand[0]#从最小的开始
                for i in range(W):#一个个的递增，因为是要搞连续的，所以直接加就行了
                    hand.remove(base+i)#如果可以连续分离，那么就成功了
            except:
                return False
        return True
    
if __name__ == "__main__":
    print(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8], 3))