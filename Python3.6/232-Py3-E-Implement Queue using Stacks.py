# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:01:06 2019

@author: hjiang
"""

"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, 
peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate 
a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, 
no pop or peek operations will be called on an empty queue).
https://blog.csdn.net/fuxuemingzhu/article/details/51345762
And other refers
用向右pop实现queue的左向pop

155， 232， 225 这三个属于相互实现的题，要注意
"""
#push O(1), pop amortized O(1)
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()# s2是反的s1

    def peek(self):# s1最前面的数，把s1倒置一下，输入s2即可
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2


class MyQueue1(object):# 自己写的，也可以通过，感觉有点靠不住，因为题目要求只能用基本操作， pop(0)不是基本操作

    def __init__(self):

        self.stack1 = []

    def push(self, x):

        self.stack1.append(x)

    def pop(self):

        return self.stack1.pop(0)

    def peek(self):
 
        return self.stack1[0]

    def empty(self):
 
        return not self.stack1