# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:27:23 2019

@author: hjiang
"""

"""
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

 

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
 

Notes:

Please remember to RESET your class variables declared in Vector2D, 
as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume that next() call will always be valid, that is, 
there will be at least a next element in the 2d vector when next() is called.
 

Follow up:

As an added challenge, try to code it using only iterators in C++ or iterators in Java.
https://leetcode.com/problems/flatten-2d-vector/discuss/168602/Python-iterator-Solution
"""
class Vector2D(object):#需要仔细查一下yield的用法

    def __init__(self, a):
        def it():
            for line in a:
                for val in line:
                    self.size -= 1
                    yield val   
										
        self.it = it()
        self.size = sum(len(line) for line in a)

    def next(self):
        return next(self.it)

    def hasNext(self):
        return self.size
#https://leetcode.com/problems/flatten-2d-vector/discuss/67653/My-Python-Solution    
class Vector2D:#感觉很机智，这种题目还要多练习
    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.col = 0
        self.row = 0
        self.vec = vec2d
        
    # @return {integer}
    def next(self):
        if self.hasNext():
            result = self.vec[self.row][self.col]
            self.col += 1
            return result

    # @return {boolean}
    def hasNext(self):
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True
            
            self.col = 0
            self.row += 1
            
        return False