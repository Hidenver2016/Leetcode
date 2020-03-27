# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:08:47 2019

@author: hjiang
"""

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.
https://blog.csdn.net/fuxuemingzhu/article/details/80787528
https://www.cnblogs.com/grandyang/p/4261431.html

更好地一个做法是使用hashtable，在这个hash表里，记录了老链表和新链表的每一组对应。这样先构造了一个纯next的链表，然后再次循环就能得到带random的链表了。
所以我们可以考虑用 HashMap 来缩短查找时间，第一遍遍历生成所有新节点时同时建立一个原节点和新节点的 HashMap，第二遍给随机指针赋值时，查找时间是常数级。
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        nodeDict = dict()
        dummy = Node(0, None, None)
        nodeDict[head] = dummy
        newHead, pointer = dummy, head# 这个newhead用来建立新链表，pointer是旧链表
        while pointer:#常规操作，循环链表，把普通部分存入hashtable 或者叫dict
            node = Node(pointer.val, pointer.next, None)
            nodeDict[pointer] = node
            newHead.next = node# 建立一个新的链表，只保存val和next
            newHead, pointer = newHead.next, pointer.next
        pointer = head#指向旧的head
        while pointer:
            if pointer.random:
                nodeDict[pointer].random = nodeDict[pointer.random]#这个是亮点，加上了random属性。 左侧是新造的节点的random属性， 右侧是在存好的hashmap中寻找
            pointer = pointer.next
        return dummy.next# 这里返回 nodeDict[head]的时候要注意第一个值 nodeDict[head] = dummy， 这里不对，其他都是对的














