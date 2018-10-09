# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:33:47 2018

@author: hjiang
"""

#Given an integer, write a function to determine if it is a power of two.

#Example 1:
#
#Input: 1
#Output: true 
#Explanation: 20 = 1
#Example 2:
#
#Input: 16
#Output: true
#Explanation: 24 = 16
#Example 3:
#
#Input: 218
#Output: false

def powerof2(num):
    for i in range(-31, 31):
        if 2**i == num:
            return True
    return False

def powerof2_1(num):
    start, end = -5, 5
    while start<= end:
        mid = int(start + (end-start)/2)
        compare = 2**mid
        if num < compare:
            end = mid-1
        elif num > compare:
            start = mid+1
        else:
            return True
    return False

def powerof2_2(num):
    return num>0 and (num & (num-1)) == 0

def powerof2_3(num):
    return num>0 and (num & ~-num) == 0

import math
def powerof2_4(num):
    sign = int(math.log(0x7fffffff)/math.log(2))
    sign1 = 2**sign % num == 0
    return num > 0 and sign1

if __name__ == "__main__":
    print(powerof2_1(0))