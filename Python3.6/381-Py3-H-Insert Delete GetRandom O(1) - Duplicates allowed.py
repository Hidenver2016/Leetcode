# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:08:15 2019

@author: hjiang
"""

"""
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. 
The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();

如果要时间为1，那么思路和380一样，还是交换位置，然后弹出最后的
这个题目有重复元素，那么就
"""

import random, collections

class RandomizedCollection(object):

    def __init__(self):
        self.vals, self.idxs = [], collections.defaultdict(set)
        

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1
        

    def remove(self, val):#过程比较复杂
        if self.idxs[val]:#先判断有没有
            out, ins = self.idxs[val].pop(), self.vals[-1]# 例如 vals=[a,b,a,c], idx = {'a':{0,2}, 'b':{1}, 'c':{3}} 那么out = 0，ins = 'c'
            self.vals[out] = ins#先把最后一个值保存在要删除的值的位置， val = [c,b,a,c]
#            if self.idxs[ins]:
            self.idxs[ins].add(out)#更新idxs idx = {'a':{2}, 'b':{1}, 'c':{0,3}}
            self.idxs[ins].discard(len(self.vals) - 1)# 更新idx idx = {'a':{2}, 'b':{1}, 'c':{0}}
            self.vals.pop()# 更新vals, vals = [c,b,a]
            return True
        return False 

    def getRandom(self):
        return random.choice(self.vals)
    
    
    
    
    
    
    
    
    