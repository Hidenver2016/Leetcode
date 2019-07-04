# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:22:07 2019

@author: hjiang
"""

"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
import collections
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        
        self.data = collections.deque(maxlen = size)       

    def next(self, val: int) -> float:        
        self.data.append(val)
        return sum(self.data)/len(self.data)
