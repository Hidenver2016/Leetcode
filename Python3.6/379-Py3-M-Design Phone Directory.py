# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:49:40 2019

@author: hjiang
"""
"""
Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);
https://leetcode.com/problems/design-phone-directory/discuss/85341/4-line-Python-solution-using-only-1-set-and-no-queue
"""
class PhoneDirectory:
    def __init__(self, maxNumbers):
        self.available = set(range(maxNumbers))

    def get(self):
        return self.available.pop() if self.available else -1

    def check(self, number):
        return number in self.available

    def release(self, number):
        self.available.add(number)
