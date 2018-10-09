# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 23:02:44 2018

@author: hjiang
"""

#Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), 
#where h is the height of the person and k is the number of people in front of this person who have a height greater 
#than or equal to h. Write an algorithm to reconstruct the queue.
#
#Note:
#The number of people is less than 1,100.
#
#
#Example
#
#Input:
#[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
#Output:
#[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

#%% solution 1
# -*- coding: utf-8 -*-

output = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

people = [[7,2], [7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

#people.sort(key=lambda (h, k): (-h, k))
people1 = sorted(people, key = lambda person: -person[0])

result = []
for p in people1:
    result.insert(p[1], p)
    
print (result)    
#if result == output:
#    print(True)
