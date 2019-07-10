# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:01:24 2018

@author: hjiang
"""

#Design and implement a data structure for Least Recently Used (LRU) cache. 
#It should support the following operations: get and put.
#
#get(key) - Get the value (will always be positive) of the key if the key exists in the cache, 
#otherwise return -1.
#put(key, value) - Set or insert the value if the key is not already present. 
#When the cache reached its capacity, it should invalidate the least recently used item 
#before inserting a new item.
#
#Follow up:
#Could you do both operations in O(1) time complexity?
#
#Example:
#
#LRUCache cache = new LRUCache( 2 /* capacity */ );
#
#cache.put(1, 1);
#cache.put(2, 2);
#cache.get(1);       // returns 1
#cache.put(3, 3);    // evicts key 2
#cache.get(2);       // returns -1 (not found)
#cache.put(4, 4);    // evicts key 1
#cache.get(1);       // returns -1 (not found)
#cache.get(3);       // returns 3
#cache.get(4);       // returns 4

#class LRUCache(object):
#
#    def __init__(self, capacity):
#        """
#        :type capacity: int
#        """
#        
#
#    def get(self, key):
#        """
#        :type key: int
#        :rtype: int
#        """
#        
#
#    def put(self, key, value):
#        """
#        :type key: int
#        :type value: int
#        :rtype: void
#        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#https://blog.csdn.net/laughing2333/article/details/70231547
#https://blog.csdn.net/qq490691606/article/details/49948263



class ListNode(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, node): #永远从后面插入
        node.next, node.prev = None, None  # avoid dirty node
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node # node 换一个名字 self.tail
            
    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next, node.prev = None, None  # make node clean

class LRUCache(object):

    # @param capacity, an integer
    def __init__(self, capacity):
        self.list = LinkedList()
        self.dict = {} # 这个hash table是用来满足o(1)查找的
        self.capacity = capacity
        
    def _insert(self, key, val):
        node = ListNode(key, val)
        self.list.insert(node)
        self.dict[key] = node
        

    # @return an integer 访问一次，我就重新在insert一次，insert永远在最后插入
    def get(self, key):
        if key in self.dict:
            val = self.dict[key].val
            self.list.delete(self.dict[key])
            self._insert(key, val)
            return val
        return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing # list 用 delete， dict 用 del
    def put(self, key, val):
        if key in self.dict:
            self.list.delete(self.dict[key])
        elif len(self.dict) == self.capacity:
            del self.dict[self.list.head.key]
            self.list.delete(self.list.head)
        self._insert(key, val)
 
 
import collections
class LRUCache2(object):#看这个把，搞清楚OrderedDict()
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        return val

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

        
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1);
    cache.put(2, 2);
    print(cache.get(1));       #// returns 1
    cache.put(3, 3);    #// evicts key 2
    print(cache.get(2));       #// returns -1 (not found)
    cache.put(4, 4);    #// evicts key 1
    print(cache.get(1));       #// returns -1 (not found)
    print(cache.get(3));       #// returns 3
    print(cache.get(4));       #// returns 4