# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:52:30 2019

@author: hjiang
"""

"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. 
The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. 
The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" 
to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) 
by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. 
Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. 
Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
"""

# Time:  O(n)
# Space: O(1)
"""
http://www.cnblogs.com/grandyang/p/5310649.html
下面这种方法是网上比较流行的一种方法，设定候选人res为0，原理是先遍历一遍，对于遍历到的人i，
若候选人res认识i，则将候选人res设为i，完成一遍遍历后，我们来检测候选人res是否真正是名人，
我们如果判断不是名人，则返回-1，如果并没有冲突，返回res，
"""
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        # Find the candidate.
        for i in range(1, n):
            if knows(candidate, i):  # noqa candidats 认识 i
                candidate = i        # All candidates < i are not celebrity candidates.
        # Verify the candidate.
        for i in range(n):
            candidate_knows_i = knows(candidate, i) # noqa 
            i_knows_candidate = knows(i, candidate) # noqa
            if i != candidate and (candidate_knows_i or not i_knows_candidate):
                return -1
        return candidate
    

class Solution1:
    def findCelebrity(self,n):
        res = [True] * n
        for i in range(len(res)):
            for j in range(len(res)):
                if res[i] and j != i:
                    if knows(i, j) or not knows(j, i):
                        res[i] = False
                        break
                    else:#此行可以注释掉
                        res[j] = False#此行也可以注释掉，因为这个反例（上面那个if语句）有点难想
            if res[i]: return i
        return -1
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
        