# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:00:10 2019

@author: hjiang
"""

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
https://blog.csdn.net/fuxuemingzhu/article/details/79253237

155， 232， 225 这三个属于相互实现的题，要注意
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1], x))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
    
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2); print(minStack.stack, minStack.min)
    minStack.push(0); print(minStack.stack, minStack.min)
    minStack.push(-3); print(minStack.stack, minStack.min)
    minStack.getMin(); print(minStack.stack, minStack.min)#   --> Returns -3.
    minStack.pop(); print(minStack.stack, minStack.min)
    minStack.top(); print(minStack.stack, minStack.min)#      --> Returns 0.
    minStack.getMin(); print(minStack.stack, minStack.min)#   --> Returns -2.