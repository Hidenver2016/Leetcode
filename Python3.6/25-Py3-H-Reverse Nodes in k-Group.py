# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:59:05 2019

@author: hjiang
"""

"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l# r, l 是4， 1
                for _ in range(k):
    #                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                    cur.next, pre, cur = pre, cur, cur.next#最后pre是3， cur是4
                jump.next, jump, l = pre, l, r  # connect two k-groups, 连接0—>3, 然后jump移动到1， l移动到4 （下一次再把1连到6）
            else:
                return dummy.next
        
    
        
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print (Solution().reverseKGroup(head,3))
    
    
    
    
    
    
    
    
    
    
    
    
    