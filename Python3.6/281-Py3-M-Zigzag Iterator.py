# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:25:09 2019

@author: hjiang
"""

"""
Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 

Output: [1,3,2,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,3,2,4,5,6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. 
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
"""
# Time:  O(n)
# Space: O(k)
import collections
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your q structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = collections.deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self):
        """
        :rtype: int
        """
        len, iter = self.q.popleft()
        if len > 1:
            self.q.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.q)
import itertools    
class ZigzagIterator(object):#这个比较快

    def __init__(self, v1, v2):
        self.vals = (v[i] for i in itertools.count() for v in (v1, v2) if i < len(v))
        self.n = len(v1) + len(v2)

    def next(self):
        self.n -= 1
        return next(self.vals)

    def hasNext(self):
        return self.n > 0
    
    
if __name__ == "__main__":
    v1 = [1,2]
    v2 = [3,4,5,6]
    v3 = [7,8]
    myclass = ZigzagIterator(v1, v2)
#    myiter = iter(myclass)
    for i in range(len(v1)+len(v2)):
        print(myclass.next())
     

    
    
    
    
    
    
    
    
    
    
    
    
    
    