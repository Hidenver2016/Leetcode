# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:36:28 2019

@author: hjiang
"""

"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""

class TwoSum:
    def __init__(self):
        self.ctr = {}

    def add(self, number):
        if number in self.ctr:
            self.ctr[number] += 1
        else:
            self.ctr[number] = 1

    def find(self, value):
        ctr = self.ctr
        for num in ctr:
            if value - num in ctr and (value - num != num or ctr[num] > 1):#此处是防止有3和6的情况，要两个3才可以
                return True
        return False
    
if __name__ == "__main__":
    test1 = TwoSum()
    test1.add(1)
    test1.add(3)
    test1.add(5)
    print(test1.find(4))
    print(test1.find(5))