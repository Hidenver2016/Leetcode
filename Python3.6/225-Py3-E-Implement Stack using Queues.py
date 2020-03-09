# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:01:11 2019

@author: hjiang
"""

"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, 
peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. 
You may simulate a queue by using a list or deque (double-ended queue), 
as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, 
no pop or top operations will be called on an empty stack).
https://blog.csdn.net/fuxuemingzhu/article/details/72598111
用queue的popleft来操作stack的pop

155， 232， 225 这三个属于相互实现的题，要注意
"""
import collections
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.que.append(x)
        for i in range(len(self.que) - 1):#把stack倒向， 把前面n-1个弹出，然后在最后加进去
            self.que.append(self.que.popleft())
            
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.que.popleft()
    
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.que[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.que
if __name__ == "__main__":
    mystack = MyStack()
    mystack.push(1); print(mystack.que)
    mystack.push(2); print(mystack.que)
    mystack.push(3); print(mystack.que)
    mystack.top(); print(mystack.que)#   // returns 2
    mystack.pop(); print(mystack.que)#   // returns 2
    mystack.empty(); print(mystack.que)# // returns false
    
    
    
    
    
    
    
    
    
    
    
    
    