# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:00:52 2019

@author: hjiang
"""

"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
https://blog.csdn.net/fuxuemingzhu/article/details/79488113

随机从链表中抽出一个节点的数字。
"""
class Solution(object):#这个更快，真是奇怪

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.stack = []
        while head:
            self.stack.append(head.val)
            head = head.next
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        _len = len(self.stack)
        return self.stack[random.randint(0, _len - 1)]
    
#水塘采样
class Solution(object):

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0, index) is 0:
                result = node
            node = node.next
            index += 1
        return result.val