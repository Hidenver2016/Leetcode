# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:38:47 2020

@author: hjiang
"""

"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. 
If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""

from heapq import *

class MaxStack:

    def __init__(self):
        self.ls = []        # list (stack)
        self.hp = []        # heap
        self.hpd = set()    # id of items deleted in ls but not hp
        self.lsd = set()    # id of items deleted in hp but not ls
        self.id = 0

    def push(self, x):
        self.ls.append((self.id, x))
        heappush(self.hp, (-x, -self.id))
        self.id += 1

    def pop(self):
        x = self.top()
        self.hpd.add(self.ls[-1][0])
        self.ls.pop()
        return x

    def top(self):
        while self.ls[-1][0] in self.lsd:
            self.lsd.remove(self.ls[-1][0])
            self.ls.pop()
        return self.ls[-1][1]

    def peekMax(self):
        while -self.hp[0][1] in self.hpd:
            self.hpd.remove(-self.hp[0][1])
            heappop(self.hp)
        return -self.hp[0][0]

    def popMax(self):
        x = self.peekMax()
        _, nid = heappop(self.hp)
        self.lsd.add(-nid)
        return x